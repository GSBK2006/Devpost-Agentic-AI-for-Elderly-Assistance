#Install Dependencies
pip install fastapi uvicorn psycopg2-binary transformers torch

#Actual code
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

app = FastAPI(title="Elderly Assistance AI Companion")

#LLM setup
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3.1-8B-Instruct")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3.1-8B-Instruct")
agent = pipeline("text-generation", model=model, tokenizer=tokenizer)

#Request schema
class TaskRequest(BaseModel):
    task: str  # e.g., "Add metformin reminder at 8AM"

@app.post("/plan_task/")
async def plan_task(request: TaskRequest):
    prompt = f"Plan: {request.task}"
    result = agent(prompt, max_new_tokens=200)
    return {"plan": result[0]['generated_text']}

#Code to run in server
uvicorn app:app --reload
