# OpenChat 🤖

A locally-hosted AI chatbot web app built with **Streamlit** and **Ollama**, powered by Google's **Gemma 3** language model. Runs entirely on your machine — no cloud API calls, no data leaving your device.

## Features

- 💬 Conversational chat interface built with Streamlit
- 🧠 Powered by Gemma 3 running locally via Ollama
- 📄 Retrieval-Augmented Generation (RAG) — upload documents and chat with their content
- 🔒 Fully local and private — no external API keys required
- ⚡ Fast responses using local inference

## Tech Stack

- **Frontend/UI:** Streamlit
- **LLM Runtime:** Ollama
- **Model:** Gemma 3
- **Language:** Python
- **Package Manager:** uv

## Project Structure


## Prerequisites

- Python 3.13+
- [Ollama](https://ollama.com) installed and running
- Gemma 3 model pulled locally:
```bash
  ollama pull gemma3
```

## Installation

1. Clone the repository:
```bash
   git clone https://github.com/yourusername/openchat.git
   cd openchat
```

2. Create and activate a virtual environment (using uv):
```bash
   uv venv
   .venv\Scripts\activate
```

3. Install dependencies:
```bash
   uv sync
```

## Usage

Make sure Ollama is running in the background, then start the app:

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` and start chatting.

## How It Works

1. The user sends a message through the Streamlit chat interface.
2. [If RAG] Uploaded documents are processed and split into chunks, then relevant chunks are retrieved based on the query.
3. The prompt (with any retrieved context) is sent to the Gemma 3 model via Ollama.
4. The model's response is streamed back and displayed in the chat.

### Supported File Types
- PDF (.pdf)
- Word Documents (.docx)

## Screenshots

[Add a screenshot or GIF of the app here]

## Future Improvements

- [ ] [e.g., add conversation history persistence]
- [ ] [e.g., support multiple document formats]
- [ ] [e.g., add model selection dropdown]

## Author

**Muhammad Zia Ul Haq**
[LinkedIn] | [GitHub]

## License

This project is licensed under the MIT License.

"# Openchat-chatbot" 
