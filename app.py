from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer, AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import re
from fastapi.responses import FileResponse

# Initialize FastAPI app
app = FastAPI(title="Text Summarixer App", description="Text Summarization using T5", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# model & tokenizer
# model = T5ForConditionalGeneration.from_pretrained("./saved_summary_model")
# tokenizer = T5Tokenizer.from_pretrained("./saved_summary_model")
model_name = "harshadhana/text-summarizer-model"

print("Loading tokenizer...")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

print("Tokenizer loaded")

print("Loading model...")
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("Model loaded")

# device
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

model.to(device)


# Input schema for dialogue => string
class DialogueInput(BaseModel):
    dialogue: str


# for data cleaning
def clean_data(text):
    text = re.sub(r"\r\n", " ", text) # lines
    text = re.sub(r"\s+", " ", text) # spaces
    text = re.sub(r"<.*?>", " ", text) # html tags <p> <h1>
    text = text.strip().lower()
    return text

# logic for summarization
def summarize_dialogue(dialogue : str) -> str:
    dialogue = clean_data(dialogue) # clean
    t5_input_text = f"summarize: {dialogue}"

    # tokenize
    inputs = tokenizer(
        t5_input_text,
        padding="max_length",
        max_length=512,
        truncation=True,
        return_tensors="pt"
    ).to(device)

    # generate the summary => token ids
    model.to(device)
    targets = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=150,
        num_beams=4,
        early_stopping=True
    )
    
    # decoded our output
    summary = tokenizer.decode(targets[0], skip_special_tokens=True) # EOS, SEP
    return summary


# API Endpoints
@app.post("/summarize")
async def summarize(input: DialogueInput):
    summary = summarize_dialogue(input.dialogue)
    return {"summary": summary}

@app.get("/")
async def home():
    return FileResponse("index.html")