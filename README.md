# AskGenix

## Project Overview
AskGenix is a modular Python backend service that implements Retrieval-Augmented Generation (RAG) to answer user questions using knowledge base documents. It connects to MongoDB for document storage, Milvus/FAISS for vector search, and OpenAI for generating responses. The system supports document uploads (PDF, CSV, Excel), voice processing via Deepgram, and ServiceNow ticket integration for enterprise use cases.

## Architecture Overview
- **api/** — RESTful endpoints:
  - `ask.py`/`ask_snow.py`: Question-answering endpoints (standard + ServiceNow-integrated)
  - `upload.py`: File uploads to S3/MongoDB
  - `knowledge_base.py`: Knowledge base management
  - `voice.py`/`listen.py`: Voice processing endpoints
  - `chat_history.py`: Conversation history storage

- **services/** — Business logic:
  - `embedding_service.py`: Generates document embeddings (using Sentence Transformers)
  - `rag_service.py`: Core RAG pipeline (retrieval + generation)
  - `milvus_service.py`/`faiss_service.py`: Vector database integrations
  - `snow_create_ticket_service.py`: ServiceNow ticket creation
  - `reranker_service.py`: Re-ranks retrieved results
  - `file_processing.py`: Handles document chunking and parsing

- **utils/** — Helper modules:
  - File readers (PDF, CSV, Excel, DOCX)
  - Database connectors (MongoDB, S3)
  - Text chunking and LLM service wrappers

- **models/** — Data schemas:
  - `question_request.py`: Request validation model requiring `question` and `user_email`

## Tech Stack
- **Language**: Python 3.12
- **Framework**: FastAPI
- **Vector Databases**: Milvus (primary), FAISS (CPU fallback)
- **Document DB**: MongoDB
- **LLM Providers**: OpenAI (GPT-4)
- **Voice Processing**: Deepgram
- **File Storage**: AWS S3 (via `PARENT_BUCKET_NAME`)
- **Key Libraries**: 
  - LangChain ecosystem (langchain-mongodb, langchain-openai)
  - sentence-transformers (embeddings)
  - PyMuPDF (PDF processing)
  - python-docx (DOCX processing)

## Setup Instructions

### Prerequisites
- Python 3.12
- MongoDB instance (or Atlas cluster)
- Milvus server (optional if using FAISS)
- OpenAI API key
- Deepgram API key

### Environment Variables
Create a `.env` file with required values:
```
MONGO_DETAILS=mongodb://localhost:27017
OPENAI_API_KEY=your_openai_key
DEEPGRAM_API_KEY=your_deepgram_key
SECRET_KEY=your_secure_key

# Optional (defaults shown)
MILVUS_HOST=localhost
MILVUS_PORT=19530
EMBEDDING_MODEL=all-MiniLM-L6-v2
LLM_MODEL=gpt-4.1-mini-2025-04-14
PARENT_BUCKET_NAME=ask-genix-documents
```

### Installation
```bash
pip install -r requirements.txt
```

### Running Locally
```bash
uvicorn main:app --reload --port 8000
```

### Docker Deployment
```bash
docker-compose up --build
```
The service will be available at `http://localhost:8000`

## Usage
Sample API request to `/ask` endpoint:
```json
{
  "question": "What are the key features of Kubernetes?",
  "user_email": "user@example.com"
}
```

Response format:
```json
{
  "answer": "Kubernetes features...",
  "sources": [
    {"source": "k8s_overview.pdf", "page": 5}
  ]
}
```

## Deployment
1. Configure production environment variables
2. Build and deploy using provided Docker setup:
   ```bash
   docker-compose up -d --build
   ```
3. For advanced deployments, use the provided `scripts/deploy.sh` (not included in current scope)

## Logging & Troubleshooting
- Logs are handled through `logger.py` with enhanced structured logging
- Check terminal output during development
- In Docker deployments, view logs with:
  ```bash
  docker logs askgenix-server
  ```
- Critical errors appear in standard error stream with context markers

## Future Improvements / TODO
1. Implement automatic MongoDB-to-Milvus data migration (currently commented in `main.py`)
2. Add FAISS fallback when Milvus is unavailable
3. Complete ServiceNow integration error handling (partial implementation in `snow_create_ticket_service.py`)
4. Expand voice processing capabilities beyond basic transcription
5. Implement retry mechanisms for external API calls
