# Virtual TA FastAPI Project

This project provides a FastAPI-based API for querying a knowledge base built from Discourse threads and Markdown documentation. It supports semantic search using embeddings and can answer questions with sources.

## Features

- Query a knowledge base using natural language
- Uses OpenAI embeddings and LLMs via the aipipe proxy
- Supports both text and image (multimodal) queries
- Returns answers with relevant source links
- Health check endpoint

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2. Install Requirements

```sh
pip install -r requirements.txt
```

### 3. Install Playwright Browsers (if using website_downloader)

```sh
playwright install
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root with your API key:

```
API_KEY=your_actual_api_key_here
```

Or set it in your shell before running the app:

```powershell
$env:API_KEY="your_actual_api_key_here"
```

### 5. Prepare the Database

- Ensure you have the `knowledge_base.db` file in the `data/` directory.
- If not, run your data collection scripts (`discourse_downloader.py`, `website_downloader.py`,`preprocess.py`) to populate the database.

---

## Running the API

```sh
python app.py
```
or
```sh
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

---

## API Endpoints

### `/query` (POST)

Query the knowledge base.

**Request Body:**
```json
{
  "question": "Your question here",
  "image": "base64-encoded-image-optional"
}
```

**Response:**
```json
{
  "answer": "Answer text",
  "links": [
    {"url": "https://...", "text": "Relevant snippet"}
  ]
}
```

### `/health` (GET)

Check API and database health.

---

## Notes

- Make sure your API key is valid and has access to the required OpenAI endpoints via aipipe.
- For best results, keep your database up to date with the latest threads and documentation.

---

## License

[MIT](LICENSE)