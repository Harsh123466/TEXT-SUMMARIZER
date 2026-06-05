---
title: Text Summarizer App
emoji: 📝
colorFrom: violet
colorTo: blue
sdk: docker
app_port: 7860
pinned: false
---

# 📝 Text Summarizer

An AI-powered Text Summarization application built using **Hugging Face Transformers**, **FastAPI**, and a modern **HTML/CSS/JavaScript** frontend.

The application generates concise and meaningful summaries from long pieces of text using a fine-tuned transformer model, helping users quickly understand key information without reading the entire content.

## 🚀 Features

* AI-powered text summarization
* FastAPI backend for efficient inference
* Modern and responsive user interface
* Real-time summary generation
* Hugging Face Transformers integration
* Clean text preprocessing pipeline
* Easy deployment on Hugging Face Spaces

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Hugging Face Transformers
* PyTorch

### Frontend

* HTML
* CSS
* JavaScript

### Model

* Fine-tuned Transformer-based Summarization Model
* Hosted on Hugging Face Hub

## 📂 Project Structure

```text
.
├── app.py
├── requirements.txt
├── Dockerfile
├── index.html
└── README.md
```

## ⚙️ How It Works

1. User enters a long text in the input area.
2. The frontend sends the text to the FastAPI backend.
3. The backend preprocesses the text.
4. The transformer model generates a concise summary.
5. The summary is returned and displayed instantly on the webpage.

## 🔧 Installation

### Clone the Repository

```bash
git clone <repository-url>
cd text-summarizer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
uvicorn app:app --reload
```

Open your browser and visit:

```text
http://127.0.0.1:8000
```

## 📡 API Endpoint

### Generate Summary

```http
POST /summarize
```

Request Body:

```json
{
  "dialogue": "Your text goes here"
}
```

Response:

```json
{
  "summary": "Generated summary"
}
```

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience with:

* Transformer-based NLP models
* Text summarization techniques
* Hugging Face ecosystem
* FastAPI backend development
* Model inference pipelines
* API integration with frontend applications
* Deployment of AI applications

## 🌟 Future Improvements

* Multiple summarization styles
* Adjustable summary length
* PDF and document summarization
* Multi-language support
* User authentication and history
* Batch summarization

## 📜 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

Harsh Adhana

If you found this project useful, feel free to star the repository and connect with me.
