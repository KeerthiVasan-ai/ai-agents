# Stock Trading Chatbot with LangGraph + LangChain

This project demonstrates a simple conversational stock trading assistant powered by **LangGraph** and **LangChain**.  
The chatbot can:
- Fetch stock prices for given symbols.
- Ask for confirmation before buying stocks.
- Maintain conversation memory across turns.

It also demonstrates how to use **interrupts** in LangGraph for approval-based workflows.

---

## 🚀 Features
- Query stock prices (`MSFT`, `AAPL`, `AMZN`, `RIL`).
- Interactive stock purchase flow with user approval.
- Memory persistence across multiple steps in a thread.
- Uses Google’s **Gemini** model via `langchain-google-genai`.

---

## 📂 Project Structure
```
├── main.py              # Example chatbot implementation
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (e.g., API keys)
└── README.md            # Project documentation
```

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KeerthiVasan-ai/ai-agents.git
   cd stock-chatbot
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux / Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Environment Setup

Create a `.env` file in the project root with your **Google Generative AI API Key**:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Running the Example

### 📦 Dependencies

Dependencies are listed in **requirements.txt**:

Install them with:
```bash
pip install -r requirements.txt
```

Run the chatbot example script:

```bash
python main.py
```

## 📜 License
MIT License
