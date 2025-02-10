# PDF Chatbot with Gemini and RAG

A Flask-based chatbot that answers questions from multiple PDF documents using Google's Gemini and Retrieval-Augmented Generation (RAG).


## Features
- Upload multiple PDF documents.
- Chat with the bot using natural language.
- Context-aware responses powered by Gemini and RAG.
- Docker support for easy deployment.
- MVC architecture with clear separation of concerns.
- Environment variable configuration.

## Installation

### Prerequisites
- Python 3.9+
- [Poetry](https://python-poetry.org/) (recommended)
- Docker (optional)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/manarbshr/applap-assessment.git
   cd chatbot-app
   ```

2. Install dependencies with Poetry:
   ```bash
   poetry install
   ```

3. Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key
   ```

4. Get a [Gemini API key](https://aistudio.google.com/app/apikey) and add it to `.env`.

## Usage

### Run Locally
```bash
poetry run python run.py
```
Visit `http://localhost:8000` to interact with the chatbot.

### Using Docker
1. Build the Docker image:
   ```bash
   docker build -t pdf-chatbot .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 --env-file .env pdf-chatbot
   ```

## Configuration
| Environment Variable | Description                |
|----------------------|----------------------------|
| `GOOGLE_API_KEY`     | Google Gemini API key      |

## API Documentation

### Endpoints
| Endpoint  | Method | Description                     |
|-----------|--------|---------------------------------|
| `/upload` | POST   | Upload PDF files                |
| `/chat`   | POST   | Submit questions to the chatbot |

#### Example Requests
**Upload PDFs**:
```bash
curl -X POST -F "files=@document1.pdf" -F "files=@document2.pdf" http://localhost:8000/upload
```

**Chat**:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "What is the main topic?"}' http://localhost:8000/chat
```

## Project Structure
```
chatbot-app/
├── app/
│   ├── controllers/      # Flask routes
│   ├── models/           # Business logic and data models
│   ├── services/         # Gemini and embedding services
│   ├── view/             # HTML/CSS/JS templates and static files
│   └── __init__.py       # Flask app initialization
├── Dockerfile
├── pyproject.toml
├── README.md
└── requirements.txt
```

## License
MIT License. See [LICENSE](LICENSE) for details.
```

---

### Key Notes:
1. Replace `yourusername` and `your_gemini_api_key` with your actual values.
2. Add a screenshot to the `/static/images` folder if available.
3. Customize the license file as needed.

