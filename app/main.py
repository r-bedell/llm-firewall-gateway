from fastapi import FastAPI
from pydantic import BaseModel

from app.llm import call_llm

# Create the web app. The title shows up on the auto-generated docs page.
app = FastAPI(title="LLM Firewall Gateway", version="0.1.0")


# Pydantic models define the exact shape of data in and out.
# If a request doesn't match (e.g. missing "prompt"), FastAPI rejects it
# automatically - that's input validation, our first security control.
class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    response: str
    blocked: bool = False  # will become True when the firewall stops something


# A health check: a simple URL that says "I'm alive."
# Real systems (Docker, load balancers) ping this to check the service.
@app.get("/health")
def health():
    return {"status": "ok"}


# The main endpoint. Right now it just forwards to the LLM.
# In Phase 2, security checks go BEFORE call_llm (input scanning)
# and AFTER it (output scanning) - that's the whole firewall idea.
@app.post("/v1/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    answer = call_llm(req.prompt)
    return ChatResponse(response=answer)