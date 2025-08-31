from flask import Flask, request, jsonify
from backend.orchestrator import build_graph
from backend.schemas import UserRequest
from datetime import datetime

app = Flask(__name__)

# Build once (reuse the compiled langgraph workflow)
graph = build_graph()

@app.route("/plan", methods=["POST"])
def plan_trip():
    try:
        data = request.json

        # Validate input
        user_request = UserRequest(
            event_name=data["event_name"],
            start_date=datetime.strptime(data["start_date"], "%Y-%m-%d").date(),
            end_date=datetime.strptime(data["end_date"], "%Y-%m-%d").date(),
            origin=data["origin"],
            budget=data["budget"],
            preferences=data.get("preferences", "")
        )

        # Run through LangGraph
        result = graph.invoke({"user_request": user_request})

        response = {
            "event_info": result["event_info"].model_dump(),
            "travel_options": [t.model_dump() for t in result["travel_options"]],
            "stay_options": [s.model_dump() for s in result["stay_options"]],
            "itinerary": [d.model_dump() for d in result["itinerary"]],
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
