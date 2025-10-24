# Genix Nova

**Genix Nova** — An AI-powered backend that uses Retrieval-Augmented Generation (RAG) to answer enterprise queries from uploaded documents and integrated data sources.

---

## Project Overview
Genix Nova is a modular Python backend implementing RAG to deliver context-aware answers using stored documents and enterprise data.  
It integrates with MongoDB for document storage, Milvus for vector search, and OpenAI for response generation.  
The system supports document uploads (PDF, CSV, Excel, DOCX), voice transcription via Deepgram, and ServiceNow ticket creation for enterprise workflows.

---

## Architecture Overview
- **api/** — Endpoints:
  - `ask.py` / `ask_snow.py`: Question-answering APIs (standard + ServiceNow-integrated)
  - `upload.py`: Handles file uploads to S3/MongoDB
  - `knowledge_base.py`: Knowledge base and metadata management
  - `voice.py` / `listen.py`: Voice processing endpoints
  - `chat_history.py`: Stores conversation logs

- **services/** — Core business logic:
  - `embedding_service.py`: Generates document embeddings using Sentence Transformers
  - `rag_service.py`: Manages the retrieval and generation workflow
  - `milvus_service.py`: Vector database interfaces
  - `reranker_service.py`: Re-ranks retrieved results
  - `file_processing.py`: Chunking and preprocessing of input files

- **utils/** — Helper modules:
  - File readers for PDF, CSV, Excel, DOCX
  - Database connectors (MongoDB, AWS S3)
  - Text chunking and LLM service wrappers

- **models/** — Data schemas:
  - `question_request.py`: Validates input with `question` and `user_email` fields

---

## Tech Stack
- **Language:** Python 3.12  
- **Framework:** FastAPI  
- **Vector Databases:** Milvus  
- **Document DB:** MongoDB  
- **LLM Providers:** OpenAI (GPT-4)  
- **Voice Processing:** Deepgram  
- **File Storage:** AWS S3 / MongoDB  
- **Key Libraries:**  
  - LangChain (langchain-mongodb, langchain-openai)  
  - sentence-transformers  
  - PyMuPDF, python-docx  
  - uvicorn, fastapi, boto3  

---

## Setup Instructions

### Prerequisites
- Python 3.12+  
- MongoDB instance (local or Atlas)  
- Milvus server  
- OpenAI API key  
- Deepgram API key  
- Docker (optional for containerized deployment)

### Environment Variables
Create a `.env` file at the project root:

```bash
# Required
MONGO_DETAILS=mongodb://localhost:27017
OPENAI_API_KEY=your_openai_key
DEEPGRAM_API_KEY=your_deepgram_key
SECRET_KEY=your_secure_key

# Optional (defaults shown)
MILVUS_HOST=localhost
MILVUS_PORT=19530
EMBEDDING_MODEL=all-MiniLM-L6-v2
LLM_MODEL=gpt-4.1-mini-2025-04-14
PARENT_BUCKET_NAME=genix-nova-documents
```

---

## Installation Commands

**Option 1: Using pip**

```bash
pip install -r requirements.txt
```

**Option 2: Using Poetry**

```bash
poetry install
```

---

## Running Locally

```bash
# Start development server
uvicorn main:app --reload --port 8000
```

Visit: [http://localhost:8000](http://localhost:8000)

**Docker Option:**

```bash
# Build and run containers
docker-compose up --build

# Stop containers
docker-compose down
```

---

## API Endpoints

| Endpoint          | Method | Description                         |
| ----------------- | ------ | ----------------------------------- |
| `/ask`            | POST   | Query knowledge base using RAG      |
| `/ask_snow`       | POST   | Query and create ServiceNow tickets |
| `/upload`         | POST   | Upload files to knowledge base      |
| `/knowledge_base` | GET    | Retrieve document metadata          |
| `/voice`          | POST   | Process and transcribe voice input  |
| `/chat_history`   | GET    | Retrieve conversation history       |

**Sample Request:**

```bash
curl -X POST http://localhost:8000/ask \
-H "Content-Type: application/json" \
-d '{"question": "What are the key features of Kubernetes?", "user_email": "user@example.com"}'
```

**Sample Response:**

```json
{
  "answer": "Kubernetes features include scalability, declarative configuration, and automated rollouts...",
  "sources": [
    {"source": "k8s_overview.pdf", "page": 5}
  ]
}
```

---

## Deployment Commands

**Docker Deployment**

```bash
docker-compose up -d --build
```

**Manual or CI/CD Deployment**

```bash
bash scripts/deploy.sh
```

> Ensure production `.env` variables are configured.

---

## Logging & Troubleshooting

**Development logs**

```bash
tail -f logs/chatbot_2025-10-24.log
```

**Docker logs**

```bash
docker logs genix-nova-server
```

Critical errors appear in standard error stream.

---

## Future Improvements / TODO

1. Automate MongoDB → Milvus data migration
2. Add FAISS fallback for offline mode
3. Extend ServiceNow integration error handling
4. Expand voice processing capabilities beyond transcription
5. Implement retry mechanisms for unstable external API calls

---

## License

Proprietary – Internal use only. © 2025 Genix Nova


