from backend.orchestrator import build_graph
from backend.schemas import UserRequest
from datetime import date
import json

def run_full_test():
    graph = build_graph()

    # Create a mock request
    request = UserRequest(
        event_name="AI Tech Conference 2025",
        start_date=date(2025, 10, 15),
        end_date=date(2025, 10, 17),
        origin="Chennai",
        budget=20000,
        preferences="AI, networking, workshops"
    )

    # Run through the graph
    result = graph.invoke({"user_request": request})

    print("\n=== EVENT INFO ===")
    print(json.dumps(result["event_info"].model_dump(), indent=2))

    print("\n=== TRAVEL OPTIONS ===")
    for t in result["travel_options"]:
        print(json.dumps(t.model_dump(), indent=2))

    print("\n=== STAY OPTIONS ===")
    for s in result["stay_options"]:
        print(json.dumps(s.model_dump(), indent=2))

    print("\n=== ITINERARY ===")
    for d in result["itinerary"]:
        print(json.dumps(d.model_dump(), indent=2))


if __name__ == "__main__":
    run_full_test()
