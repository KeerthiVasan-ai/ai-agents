# backend/agents/event_info.py
import requests
from typing import Optional
from backend.schemas import EventInfo, EventSession, UserRequest

# Normally you would use Eventbrite/Meetup API here
# For demo, we’ll mock responses
class EventInfoAgent:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.base_url = "https://www.eventbriteapi.com/v3"  # Example

    def fetch_event(self, user_request: UserRequest) -> EventInfo:
        """
        Fetch event details from an external API (mock for now).
        """
        # ------------------------------
        # MOCK IMPLEMENTATION
        # ------------------------------
        event_data = {
            "id": "EVT123",
            "title": user_request.event_name,
            "venue": "Bangalore International Exhibition Centre",
            "address": "Tumkur Road, Bangalore",
            "start": str(user_request.start_date),
            "end": str(user_request.end_date),
            "schedule": [
                {
                    "time": "10:00 AM",
                    "title": "Opening Keynote: The Future of AI",
                    "speaker": "Dr. A. Kumar",
                    "track": "Keynote"
                },
                {
                    "time": "2:00 PM",
                    "title": "Hands-on Workshop: LangGraph for Multi-Agent AI",
                    "speaker": "Keerthivasan S",
                    "track": "Workshop"
                },
                {
                    "time": "5:00 PM",
                    "title": "Panel Discussion: AI Ethics",
                    "speaker": "Industry Leaders",
                    "track": "Panel"
                }
            ]
        }

        sessions = [EventSession(**s) for s in event_data["schedule"]]

        return EventInfo(
            id=event_data["id"],
            title=event_data["title"],
            venue=event_data["venue"],
            address=event_data["address"],
            start=event_data["start"],
            end=event_data["end"],
            schedule=sessions
        )
