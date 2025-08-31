# backend/agents/schedule_agent.py
from typing import List
from backend.schemas import UserRequest, EventInfo, TravelOption, StayOption, ItineraryDay, ItineraryItem
import google.generativeai as genai
import os
import json

class ScheduleAgent:
    def __init__(self):
        # Use API key from environment variable for security
        genai.configure(api_key=os.getenv("GENAI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def build_schedule(
        self,
        user_request: UserRequest,
        event_info: EventInfo,
        travel: List[TravelOption],
        stay: List[StayOption]
    ) -> List[ItineraryDay]:
        """
        Use Gemini to generate a daily itinerary.
        """

        # Convert structured data into text for LLM
        context = f"""
        Event: {event_info.title}
        Venue: {event_info.venue}, {event_info.address}
        Dates: {event_info.start} to {event_info.end}

        Travel Options: {json.dumps([t.dict() for t in travel], indent=2)}
        Stay Options: {json.dumps([s.dict() for s in stay], indent=2)}
        Sessions: {json.dumps([s.dict() for s in event_info.schedule], indent=2)}

        User Preferences: {user_request.preferences}
        """

        prompt = f"""
        You are a smart travel planner. Based on the event sessions, travel, and stay options, 
        create a clear day-wise itinerary. Include time, title, location, and type
        (session, meal, travel, networking, free time).
        
        Respond in JSON array of days, each with `date` and `items`.
        Example:
        [
          {{
            "date": "2025-10-15",
            "items": [
              {{
                "time": "08:00",
                "title": "Flight from Chennai to Bangalore",
                "location": "Chennai Airport",
                "type": "travel"
              }},
              {{
                "time": "10:00",
                "title": "Opening Keynote",
                "location": "Event Hall A",
                "type": "session"
              }}
            ]
          }}
        ]
        """

        # ✅ Gemini API call (no self.client, no completions)
        response = self.model.generate_content(context + "\n\n" + prompt,generation_config={"response_mime_type": "application/json"})

        # Gemini returns text
        raw_output = response.text.strip()

        try:
            parsed = json.loads(raw_output)
        except Exception as e:
            raise ValueError(f"Failed to parse Gemini output: {raw_output}") from e

        itinerary = []
        for day in parsed:
            items = [ItineraryItem(**i) for i in day["items"]]
            itinerary.append(ItineraryDay(date=day["date"], items=items))

        return itinerary
