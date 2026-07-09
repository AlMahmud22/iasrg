
1
PROJECT MANUAL – IQA CHATBOT SYSTEM
Created By: TANSHIBA NAORIN PRAPTI
Matric: A20EC4051
Date: 16 JULY 2025
1 PROJECT OVERVIEW
The IQA Chatbot System is built to handle uploaded PDF documents by automatically parsing,
chunking, and converting them into embeddings. These processed data chunks are then served via a
chatbot interface powered by the Mistral 7B model through Ollama. The architecture is lightweight,
modular, and easily extendable — enabling straightforward upgrades to both the backend logic and
the language model with minimal changes.
2 DATABASE STRUCTURE (MONGODB)
Database Name: iqa
The system uses the following collections in the MongoDB database:
Collection Name Description
activities Tracks user activity and system-level events.
apis Stores API endpoints and configurations including the
Mistral Ollama setup.
chats Saves user-chatbot interactions for history or analytics.
logs General system logs.
logs_admins Specific logs related to admin operations.
logs_sysadmins Logs related to sysadmin functions and errors.
logs_users User interaction logs.
logs_visitors Tracks Non-Admin Users who are solely entitled to use
the chatbot only.
portable Contains uploaded PDF files and their chun-
ked/preprocessed data.
settings Stores platform-wide or model-specific configuration.
trash Temporary or deleted data.
trashes Backup or log of deleted entries for recovery/audit.
updates Tracks system updates or model changes.
users User account data and roles.
3 PDF UPLOAD AND PROCESSING
Uploaded PDFs are handled in the portable collection. Each file is automatically:
•Stored in the database
•Parsed and chunked
•Preprocessed into embeddings usable by the chatbot
4 LLM INTEGRATION – OLLAMA + MISTRAL 7B
The system uses Mistral 7B, integrated via Ollama.
4.1 Setup Steps
1. Install Ollama from: https://ollama.com
2. Download the model:
ollama pull mistral
3. Verify Ollama is active:
ollama ps
4. Serve the model:
ollama run mistral
ollama list
4.2 Model Switching
The apis collection contains the model endpoint (http://localhost:11434/api/generate) and config-
uration JSON. Switching models only requires updating these fields—no backend changes required.
5 MODEL SPECIFICATIONS & SYSTEM REQUIREMENTS
Model Parameters Quantization VRAM
(Min/Recommended)
Use Case
Mistral 7B 7B Q4 6 GB / 8 GB Fast and accurate for
general usage
all-
minilm:latest
1B N/A 512 MB / 1 GB Lightweight; good for
sentence embeddings
nomic-embed-
text:latest
1B+ N/A 1 GB / 2 GB Versatile embedding
model; useful for large
document search
6 DEPLOYMENT ON UTM SERVER
Important: This project is complete. The following steps cover only placing the system on a
production server.
1. Access a Linux server (Ubuntu 20.04 or 22.04 preferred)
2. Clone the repository:
git clone https://github.com/Tanshiba12/IQA_tail.git
