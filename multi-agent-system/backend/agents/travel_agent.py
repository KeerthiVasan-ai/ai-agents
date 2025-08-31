# backend/agents/travel_agent.py
from typing import List
from datetime import datetime
from backend.schemas import UserRequest, TravelOption

class TravelAgent:
    def __init__(self):
        # Later: connect to Skyscanner, Rome2Rio, or Amadeus APIs
        pass

    def fetch_travel_options(self, user_request: UserRequest) -> List[TravelOption]:
        """
        Mock travel options based on origin and event city.
        """
        # For now, assume event is in Bangalore
        destination = "Bangalore"
        travel_date = user_request.start_date

        mock_options = [
            TravelOption(
                mode="flight",
                departure=f"{user_request.origin} Airport",
                arrival="Kempegowda Intl Airport, Bangalore",
                duration_minutes=85,
                price=5500,
                provider="IndiGo"
            ),
            TravelOption(
                mode="train",
                departure=f"{user_request.origin} Railway Station",
                arrival="Bangalore City Junction",
                duration_minutes=360,
                price=1200,
                provider="Indian Railways"
            ),
            TravelOption(
                mode="bus",
                departure=f"{user_request.origin} Bus Stand",
                arrival="Majestic Bus Stand, Bangalore",
                duration_minutes=420,
                price=800,
                provider="KSRTC"
            )
        ]

        return mock_options
