# Adaptive AI Mock Test Engine & Personal Tutor

Phase 1 establishes the database foundation for the zero-cost educational
architecture.

## Architecture

- Streamlit: UI and orchestration
- Neon PostgreSQL: persistent application data
- Cloudflare R2: large-file storage (Phase 2)
- Gemini: document/vision intelligence (Phase 3+)
- Groq GPT-OSS 120B: advanced reasoning and grading (Phase 3+)
- Python/SymPy: deterministic numerical verification (Phase 4+)
- Hugging Face: optional local embeddings/experiments

## Phase 1 goals

1. Connect Python to Neon PostgreSQL.
2. Verify the existing schema.
3. Provide repositories for users, subjects and topics.
4. Provide a Streamlit health-check screen.
5. Establish a GitHub-safe configuration pattern.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and set DATABASE_URL
streamlit run app.py
```

## Neon

The database schema has already been executed successfully in Neon.

The canonical schema is stored at:

`database/schema.sql`

Do not re-run the schema unnecessarily in production.

## Next implementation phases

Phase 2: R2 storage + document ingestion
Phase 3: AI provider interfaces + router
Phase 4: RAG / pgvector
Phase 5: mock-test generation
Phase 6: handwritten-answer transcription/evaluation
Phase 7: mastery / grey-area engine
Phase 8: persistent tutor
Phase 9: quotas, caching, observability, deployment hardening
