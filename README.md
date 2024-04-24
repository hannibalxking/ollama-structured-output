# 🌟 Ollama Structured Output Examples

This enchanted repository demonstrates how to use Ollama with Pydantic to produce structured outputs from a language model, including basic examples, pet management, image analysis, and a Flask API.

## 🎯 Overview

- **Basic**: Fetch structured country information.
- **Pets Management**: Extract pet data from natural language descriptions.
- **Vision**: Analyze pets in images (code provided in examples).
- **API**: Flask server exposing endpoints for pet management.

## 🏰 Installation

First, clone the repository:

```bash
git clone https://github.com/${GITHUB_REPOSITORY}.git
cd ollama-structured-output
```

Create a Python environment:

```bash
python -m venv venv
# Windows
.\venv\Scripts\Activate
# Unix/MacOS
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔮 Configuration

Copy the example environment file and adjust as needed:

```bash
copy .env.example .env
```

## ⚔️ Usage

### Basic Country Example

```bash
python src/basics.py
```

### Pets Management Example

```bash
python src/pets_example.py
```

### Flask API

Start the server:

```bash
python src/api.py
```

- `POST /pets` to add with JSON `{ "description": "..." }`
- `GET /pets` to list
- `GET/PUT/DELETE /pets/<name>`
- `POST /analyze` for bulk analysis

## 🧪 Testing

Run the test suite:

```bash
pytest
```

## ⚡ Notes

- Ensure Ollama is running locally on specified base URL in `.env`.
- Models defined in `src/models.py`.

May your outputs always be structured and your code ever robust! 🌟