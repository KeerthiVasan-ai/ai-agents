# AI-Powered Multi-Agent Travel Planner

This project is a demo of a **Multi-Agent System** for planning travel to an event.  
It uses a **Flask backend** for orchestration and a **Streamlit frontend** for the user interface.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/KeerthiVasan-ai/ai-agents.git
cd multi-agent-system
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate   # On Windows
# OR
source .venv/bin/activate  # On Linux/Mac

```

### 3. Install UV & install dependencies
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" #Windows

uv install
```

## 🔑 Environment Setup

Create a `.env` file in the project root with your **Google Generative AI API Key**:

```
GOOGLE_API_KEY=your_api_key_here
```

---

### 4. Run the backend (Flask)
```bash
python backend/app.py
```

This will start the backend server at:
```
http://127.0.0.1:8000
```

### 5. Run the frontend (Streamlit)
In a new terminal (with the same virtual environment activated):
```bash
streamlit run frontend/streamlit_app.py
```

This will open the UI in your browser.

---

## 📂 Project Structure
```
multi-agent-system/
│── backend/        # Flask backend with orchestrator & agents
│── frontend/       # Streamlit frontend
│── requirements.txt
│── README.md
```

---

## ✅ Example Usage
1. Open the Streamlit app in your browser.  
2. Enter your **event name, dates, origin city, budget, and preferences**.  
3. The system will generate:
   - 📌 Event details  
   - 🚆 Travel options  
   - 🏨 Stay recommendations  
   - 📅 Full itinerary  

---

## 🛠 Tech Stack
- **Python** (Flask, Streamlit)  
- **LangGraph + Gemini/OpenAI** for multi-agent orchestration  
- **REST API** backend with **interactive UI** frontend  

---

## ⚡ Run in one line
Backend:
```bash
python backend/app.py
```

Frontend:
```bash
streamlit run frontend/app.py
```
