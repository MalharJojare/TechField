# 🧠 Instagram AI Reply Bot

An intelligent **Instagram DM auto-reply bot** that analyzes incoming messages using AI and responds with either a **relevant meme + caption** or a **sarcastic text reply** — all powered by a LangGraph workflow.

---

## ✨ Features

- **AI-Powered Message Analysis** — Extracts topic, emotion, keywords, and humor style using OpenAI structured outputs
- **Smart Meme Search** — Queries Giphy with keyword combinations and scores results for relevance
- **Adaptive Responses** — Sends a meme + caption if a good match is found, otherwise falls back to a sarcastic text reply
- **Conversation Memory** — Stores chat history in PostgreSQL for context-aware replies
- **FastAPI Server** — REST API endpoint (`POST /reply`) for easy integration
- **Chrome Extension** — Browser extension for Instagram web integration (WIP)
- **LangGraph Workflow** — Modular, state-machine-based pipeline for extensibility

---

## 🏗️ Architecture

```
Message In → [Memory Loader] → [Analyzer] → [Meme Search] → [Caption] or [Sarcasm] → [Memory Saver] → Reply Out
```

### Workflow Nodes

| Node | Purpose |
|---|---|
| `memory_loader` | Fetches last 10 conversations for context |
| `analyzer` | OpenAI extracts topic, emotion, keywords, humor_style |
| `meme_search` | Searches Giphy API with keyword combinations |
| `caption` | OpenAI generates a funny meme caption |
| `sarcasm` | OpenAI generates a sarcastic text reply |
| `memory_saver` | Saves the conversation to PostgreSQL |

### Project Structure

```
insta-ai-reply-bot/
├── agents/                  # AI agent nodes
│   ├── analyzer.py          # Message analysis (OpenAI structured outputs)
│   ├── meme_search.py       # Giphy meme search + scoring
│   ├── caption.py           # Meme caption generation
│   └── sarcasm.py           # Sarcastic reply generation
├── app/                     # FastAPI application
│   ├── main.py              # FastAPI server with POST /reply
│   └── schemas.py           # Pydantic request/response models
├── graph/                   # LangGraph workflow
│   ├── state.py             # AgentState TypedDict
│   ├── workflow.py          # Workflow graph definition (6 nodes)
│   └── memory_nodes.py      # Memory loader/saver nodes
├── insta-ai-extension/      # Chrome extension (WIP)
│   ├── manifest.json        # Extension manifest v3
│   └── popup.html           # Extension popup UI
├── instagram/               # Instagram automation (WIP)
│   ├── client.py            # Playwright browser client
│   ├── listener.py          # Message listener (stub)
│   └── sender.py            # Message sender (stub)
├── memory/                  # Database layer
│   ├── database.py          # SQLAlchemy engine & session
│   ├── models.py            # ORM: User, Conversation, AgentState
│   ├── repository.py        # Conversation CRUD operations
│   └── service.py           # Conversation persistence helper
├── services/                # Service layer
│   ├── bot_service.py       # Workflow invocation & response assembly
│   ├── giphy_service.py     # Giphy API client
│   ├── llm.py               # OpenAI wrapper
│   ├── openai_service.py    # OpenAI wrapper with rate-limit handling
│   └── user_service.py      # User get-or-create
├── tests/                   # Test suite
│   ├── test_analyzer.py
│   ├── test_bot_service.py
│   ├── test_database.py
│   ├── test_instagram_login.py
│   ├── test_meme_search.py
│   ├── test_memory.py
│   ├── test_openai.py
│   └── test_workflow.py
├── main.py                  # CLI entry point
├── config.py                # Environment-based configuration
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variable template
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- **PostgreSQL** database
- **OpenAI API key** — [Get one here](https://platform.openai.com/api-keys)
- **Giphy API key** — [Get one here](https://developers.giphy.com)

### Installation

```bash
# Clone or navigate to the project
cd insta-ai-reply-bot

# Create and activate virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright (for Instagram browser automation)
pip install playwright
playwright install chromium
```

### Configuration

```bash
# Copy the environment template
cp .env.example .env
# Windows:
# copy .env.example .env
```

Edit `.env` with your credentials:

```env
OPENAI_API_KEY=sk-your-openai-api-key-here
GIPHY_API_KEY=your-giphy-api-key-here
DATABASE_URL=postgresql://username:password@localhost:5432/instagram_bot
OPENAI_MODEL=gpt-4.1-mini
```

### Database Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE instagram_bot;
```

---

## 🎮 Usage

### Start the API Server

```bash
uvicorn app.main:app --reload --port 8000
```

### Send a Message

```bash
curl -X POST http://127.0.0.1:8000/reply \
  -H "Content-Type: application/json" \
  -d '{
    "instagram_id": "user123",
    "message": "My boss scheduled another useless meeting"
  }'
```

### Example Response

```json
{
  "reply": "Quick, hide under the desk before they assign action items! 🏃",
  "meme_url": "https://media2.giphy.com/media/.../giphy.gif",
  "meme_title": "meeting meme GIF",
  "response_type": "meme"
}
```

### Run Tests

```bash
python -m pytest tests/ -v
```

---

## 🔧 API Reference

### `POST /reply`

**Request Body:**
| Field | Type | Description |
|---|---|---|
| `instagram_id` | `string` | Unique identifier for the Instagram user |
| `message` | `string` | The incoming DM message text |

**Response Body:**
| Field | Type | Description |
|---|---|---|
| `reply` | `string` | The generated reply text |
| `meme_url` | `string\|null` | URL of the matched GIF/meme |
| `meme_title` | `string\|null` | Title of the matched GIF/meme |
| `response_type` | `string` | `"meme"` if a meme was sent, `"sarcasm"` otherwise |

---

## 🐛 Known Issues

| Issue | Status |
|---|---|
| Instagram `listener.py` and `sender.py` are empty stubs | ⏳ Incomplete |
| Chrome extension `popup.js` and `content.js` are missing | ⏳ Incomplete |
| `workflow/` directory is empty | ⏳ Not implemented |
| `playwright` missing from `requirements.txt` | ✅ Fixed |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.10+** | Core language |
| **FastAPI** | REST API server |
| **LangGraph** | Workflow / state machine |
| **OpenAI API** | Message analysis & text generation |
| **Giphy API** | Meme / GIF search |
| **SQLAlchemy** | ORM for PostgreSQL |
| **PostgreSQL** | Conversation & user storage |
| **Playwright** | Instagram browser automation |
| **Pydantic** | Data validation |

---

## 📝 License

This project is for educational and personal use. Ensure compliance with Instagram's Terms of Service before deploying.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

