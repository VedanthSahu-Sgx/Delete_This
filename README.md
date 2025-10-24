# AskGenix



**AskGenix** — An AI-powered backend that uses Retrieval-Augmented Generation (RAG) to answer enterprise queries from uploaded documents and integrated data sources.



---



## Project Overview
AskGenix is a modular Python backend that implements Retrieval-Augmented Generation (RAG) to deliver context-aware answers using stored documents and enterprise data.  
It integrates with MongoDB for document storage, Milvus/FAISS for vector search, and OpenAI for response generation.  
The system supports document uploads (PDF, CSV, Excel), voice transcription via Deepgram, and ServiceNow ticket creation for enterprise workflows.



---



## Architecture Overview
- **api/** — endpoints:
  - `ask.py` / `ask_snow.py`: Question-answering APIs (standard + ServiceNow-integrated)
  - `upload.py`: Handles file uploads to S3/MongoDB
  - `knowledge_base.py`: Knowledge base and metadata management
  - `voice.py` / `listen.py`: Voice processing endpoints
  - `chat_history.py`: Stores conversation logs



- **services/** — Core business logic:
  - `embedding_service.py`: Generates document embeddings using Sentence Transformers
  - `rag_service.py`: Manages the retrieval and generation workflow
  - `milvus_service.py` : Vector database interfaces
  - `reranker_service.py`: Re-ranks retrieved results
  - `snow_create_ticket_service.py`: ServiceNow ticket creation
  - `file_processing.py`: Chunking and preprocessing of input files



- **utils/** — Helper modules:
  - File readers for PDF, CSV, Excel, and DOCX
  - Database connectors (MongoDB, AWS S3)
  - Text chunking and LLM service wrappers



- **models/** — Data schemas:
  - `question_request.py`: Validates input with `question` and `user_email` fields



---



## Tech Stack
- **Language**: Python 3.12  
- **Framework**: FastAPI  
- **Vector Databases**: Milvus  
- **Document DB**: MongoDB  
- **LLM Providers**: OpenAI (GPT-4)  
- **Voice Processing**: Deepgram  
- **File Storage**: AWS S3  
- **Key Libraries**:
  - LangChain (langchain-mongodb, langchain-openai)
  - sentence-transformers
  - PyMuPDF, python-docx
  - uvicorn, fastapi, boto3



---



## Setup Instructions



### Prerequisites
- Python 3.12+
- MongoDB instance (local or Atlas)
- Milvus server (optional if using FAISS fallback)
- OpenAI API key
- Deepgram API key



### Environment Variables
Create a `.env` file at the project root:
```bash
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
