# backend/orchestrator.py
from langgraph.graph import StateGraph, END
from backend.schemas import UserRequest, EventInfo, TravelOption
from backend.agents.event_info import EventInfoAgent
from backend.agents.travel_agent import TravelAgent
from backend.agents.stay_agent import StayAgent
from backend.schemas import StayOption
from backend.agents.schedule_agent import ScheduleAgent
from backend.schemas import ItineraryDay
from typing import List, Dict, Any

# -------------------------------
# Define shared state
# -------------------------------
class PlannerState(Dict[str, Any]):
    user_request: UserRequest
    event_info: EventInfo | None
    travel_options: List[TravelOption]
    stay_options: List[StayOption]
    itinerary: List[ItineraryDay]

# -------------------------------
# Agent Wrappers as LangGraph Nodes
# -------------------------------
def event_info_node(state: PlannerState) -> PlannerState:
    agent = EventInfoAgent()
    event_info = agent.fetch_event(state["user_request"])
    state["event_info"] = event_info
    return state

def travel_node(state: PlannerState) -> PlannerState:
    agent = TravelAgent()
    travel_options = agent.fetch_travel_options(state["user_request"])
    state["travel_options"] = travel_options
    return state

def stay_node(state: PlannerState) -> PlannerState:
    agent = StayAgent()
    stay_options = agent.fetch_stay_options(
        state["user_request"],
        state["event_info"]
    )
    state["stay_options"] = stay_options
    return state

def schedule_node(state: PlannerState) -> PlannerState:
    agent = ScheduleAgent()
    itinerary = agent.build_schedule(
        state["user_request"],
        state["event_info"],
        state["travel_options"],
        state["stay_options"]
    )
    state["itinerary"] = itinerary
    return state

# -------------------------------
# Build Graph
# -------------------------------
def build_graph():
    workflow = StateGraph(PlannerState)

    workflow.add_node("event_info", event_info_node)
    workflow.add_node("travel", travel_node)
    workflow.add_node("stay", stay_node)
    workflow.add_node("schedule", schedule_node)

    workflow.set_entry_point("event_info")
    workflow.add_edge("event_info", "travel")
    workflow.add_edge("travel", "stay")
    workflow.add_edge("stay", "schedule")
    workflow.add_edge("schedule", END)

    return workflow.compile()
