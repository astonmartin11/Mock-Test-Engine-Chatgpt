# Implementation Order

## Phase 1 — Database Foundation ✅
1. Neon PostgreSQL schema
2. Database connection
3. Repository layer
4. Health-check UI
5. GitHub-safe secrets/configuration

## Phase 2 — Storage
1. Cloudflare R2 bucket
2. R2 adapter
3. Presigned upload/download URLs
4. `documents` and `answer_artifacts` integration
5. Local text extraction
6. Processing jobs

## Phase 3 — AI Provider Layer
1. Gemini provider
2. Groq provider
3. Pydantic request/response schemas
4. Model registry lookup
5. AI router
6. retry / timeout / rate-limit handling
7. AI run + usage logging

## Phase 4 — Knowledge / RAG
1. Document chunker
2. Local embeddings
3. pgvector storage
4. hybrid retrieval
5. topic extraction
6. question evidence

## Phase 5 — Mock Test Engine
1. Adaptive topic selection
2. test configuration
3. Gemini question drafting
4. GPT-OSS validation
5. numerical verification
6. hidden solution storage
7. PDF generation

## Phase 6 — Evaluation
1. text submission
2. image/PDF submission
3. Gemini transcription
4. structured grading with GPT-OSS
5. step-level evaluation
6. mathematical verification
7. mastery update

## Phase 7 — Tutor
1. conversation storage
2. RAG context pack
3. grey-area injection
4. tutor memory
5. simple/advanced router

## Phase 8 — Hardening
1. per-user quotas
2. AI caching
3. observability
4. retry budgets
5. abuse protection
6. deployment
7. backups / migrations
