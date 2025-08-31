# backend/schemas.py
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

# -------------------------
# User Input Schema
# -------------------------
class UserRequest(BaseModel):
    event_name: str = Field(..., description="Name of the event (e.g., PyCon 2025)")
    event_id: Optional[str] = Field(None, description="Optional Eventbrite/unique ID")
    start_date: date
    end_date: date
    origin: str = Field(..., description="Origin city (e.g., Chennai)")
    budget: Optional[float] = Field(None, description="Budget in INR or USD")
    preferences: Optional[str] = Field(None, description="User preferences (AI talks, networking, food, etc.)")

# -------------------------
# Event Information
# -------------------------
class EventSession(BaseModel):
    time: str
    title: str
    speaker: Optional[str] = None
    track: Optional[str] = None

class EventInfo(BaseModel):
    id: str
    title: str
    venue: str
    address: str
    start: str
    end: str
    schedule: List[EventSession] = []

# -------------------------
# Travel Options
# -------------------------
class TravelOption(BaseModel):
    mode: str  # flight/train/bus
    departure: str
    arrival: str
    duration_minutes: int
    price: Optional[float] = None
    provider: Optional[str] = None

# -------------------------
# Stay Options
# -------------------------
class StayOption(BaseModel):
    name: str
    address: str
    distance_meters: int
    price_per_night: Optional[float] = None
    rating: Optional[float] = None

# -------------------------
# Itinerary Day Plan
# -------------------------
class ItineraryItem(BaseModel):
    time: str
    title: str
    location: Optional[str] = None
    type: Optional[str] = None  # "session", "meal", "travel", "free time"

class ItineraryDay(BaseModel):
    date: str
    items: List[ItineraryItem]

# -------------------------
# Weather Info
# -------------------------
class WeatherForecast(BaseModel):
    date: str
    condition: str
    temperature_c: float
    rain_probability: Optional[float] = None

# -------------------------
# Final Output
# -------------------------
class FinalPlan(BaseModel):
    event: EventInfo
    travel: List[TravelOption]
    stay: List[StayOption]
    itinerary: List[ItineraryDay]
    packing_list: List[str]
    weather: List[WeatherForecast]
    cost_estimate: float
