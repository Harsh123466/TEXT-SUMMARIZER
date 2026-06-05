Text Summarizer App - Transformer Minor Project using Hugging Face and FastAPI.

## Run locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000`.

## Deploy on Render

1. Push this `Text_Summarizer` repository to GitHub.
2. Create a new Render Web Service from the GitHub repository.
3. Use these settings:
   - Runtime: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - Health Check Path: `/health`
4. Add this environment variable if it is not picked up from `render.yaml`:
   - `MODEL_NAME=harshadhana/text-summarizer-model`
   - `PYTHON_VERSION=3.11.9`
   - `HF_TOKEN=your_hugging_face_access_token`

This Render app uses the Hugging Face Inference API so it does not load `torch` or the model into Render memory.
