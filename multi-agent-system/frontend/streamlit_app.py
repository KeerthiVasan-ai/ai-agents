import streamlit as st
import requests
import json

API_URL = "http://localhost:8000/plan"  # ensure backend runs on 8000

st.set_page_config(page_title="AI Travel Planner", layout="wide")

st.title("✈️ AI-Powered Multi-Agent Travel Planner")

# --- Input Form ---
with st.form("user_input"):
    event_name = st.text_input("Event Name", "AI Tech Conference 2025")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    origin = st.text_input("Origin City", "Chennai")
    budget = st.number_input("Budget (INR)", min_value=1000, value=20000, step=1000)
    preferences = st.text_area("Preferences", "AI, networking, workshops")
    
    submitted = st.form_submit_button("🚀 Generate Plan")

# --- On Submit ---
if submitted:
    payload = {
        "event_name": event_name,
        "start_date": str(start_date),
        "end_date": str(end_date),
        "origin": origin,
        "budget": budget,
        "preferences": preferences,
    }

    with st.spinner("Planning your trip... 🧳"):
        response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        data = response.json()

        # --- Event Info ---
        st.subheader("📌 Event Info")
        ev = data["event_info"]
        with st.container(border=True):
            st.markdown(f"### {ev['title']}")
            st.write(f"📍 **Venue:** {ev['venue']} — {ev['address']}")
            st.write(f"🗓️ **Dates:** {ev['start']} → {ev['end']}")
            st.write("🎤 **Schedule:**")
            for s in ev["schedule"]:
                st.markdown(f"- ⏰ {s['time']} — **{s['title']}** ({s['track']}) by {s['speaker']}")

        # --- Travel Options ---
        st.subheader("🚆 Travel Options")
        cols = st.columns(len(data["travel_options"]))
        for i, t in enumerate(data["travel_options"]):
            with cols[i]:
                with st.container(border=True):
                    st.markdown(f"### {t['mode'].title()}")
                    st.write(f"🛫 {t['departure']} → 🛬 {t['arrival']}")
                    st.write(f"⏳ {t['duration_minutes']} mins")
                    st.write(f"💰 ₹{t['price']} ({t['provider']})")

        # --- Stay Options ---
        st.subheader("🏨 Stay Options")
        cols = st.columns(len(data["stay_options"]))
        for i, s in enumerate(data["stay_options"]):
            with cols[i]:
                with st.container(border=True):
                    st.markdown(f"### {s['name']} ⭐{s['rating']}")
                    st.write(f"📍 {s['address']} ({s['distance_meters']}m from venue)")
                    st.write(f"💰 ₹{s['price_per_night']} / night")

        # --- Itinerary ---
        st.subheader("📅 Itinerary")
        for day in data["itinerary"]:
            with st.container(border=True):
                st.markdown(f"### 📆 {day['date']}")
                for item in day["items"]:
                    st.markdown(
                        f"- ⏰ **{item['time']}** — {item['title']} ({item['type']}) at {item['location']}"
                    )

    else:
        try:
            st.error(f"Error: {response.json().get('error')}")
        except:
            st.error("Unknown error occurred. Please check backend logs.")
