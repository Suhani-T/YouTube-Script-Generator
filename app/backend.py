from fastapi import FastAPI
from pydantic import BaseModel

app_instance = FastAPI(title="Script Generator API")

class Prompt(BaseModel):
    topic: str

@app_instance.post("/generate")
async def generate_script(prompt: Prompt):
    return {
        "topic": prompt.topic,
        "script": f"Prompt topic received : {prompt.topic}.\n"
    }
