# backend/agents/stay_agent.py
from typing import List
from backend.schemas import UserRequest, StayOption, EventInfo

class StayAgent:
    def __init__(self):
        # Later: plug Google Places API or Booking API
        pass

    def fetch_stay_options(self, user_request: UserRequest, event_info: EventInfo) -> List[StayOption]:
        """
        Mock accommodation options near the event venue.
        """
        # Mock hotels near Bangalore International Exhibition Centre
        mock_stays = [
            StayOption(
                name="Taj Yeshwantpur",
                address="Tumkur Road, Bangalore",
                distance_meters=2500,
                price_per_night=7500,
                rating=4.7
            ),
            StayOption(
                name="Treebo Trend Hotel",
                address="Peenya, Bangalore",
                distance_meters=3500,
                price_per_night=2500,
                rating=4.0
            ),
            StayOption(
                name="Budget Inn Residency",
                address="Rajajinagar, Bangalore",
                distance_meters=5000,
                price_per_night=1500,
                rating=3.6
            ),
        ]

        return mock_stays
