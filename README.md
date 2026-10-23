# Smart SCM — Agentic AI Integrated Supply Chain Management

Full-stack student project:
- React + Vite frontend
- FastAPI backend
- SQLite + SQLAlchemy database
- Demand, Inventory, Supplier, Procurement, Risk and Decision agents
- Optional OpenAI-compatible chat; deterministic DEMO mode works without an API key

## Run on Windows
1. Install Python 3.11+ and Node.js 20+.
2. In this folder:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
cd backend
pip install -r requirements.txt
cd ..
copy .env.example .env
```
3. Terminal 1:
```powershell
cd backend
uvicorn app.main:app --reload --port 8000
```
4. Terminal 2:
```powershell
cd frontend
npm install
npm run dev
```
5. Open the Vite URL, normally http://localhost:5173.
6. API docs: http://127.0.0.1:8000/docs

## AI
Default is `AI_PROVIDER=demo`. To use an OpenAI-compatible endpoint, set:
`AI_PROVIDER=openai`, `OPENAI_API_KEY`, and `OPENAI_MODEL` in `.env`.
The backend falls back to deterministic agent reasoning if those settings are missing.

## Agentic flow
Observe → Analyze → Reason → Decide → Recommend → Human approval

## API
GET /api/health
GET /api/dashboard
GET /api/inventory
GET /api/suppliers
GET /api/orders
POST /api/ai/analyze
POST /api/ai/chat
POST /api/seed
