# The hidden instructions a real app would give its LLM.
# Attackers often try to make the model reveal this - we'll defend it in Phase 4.
SYSTEM_PROMPT = "You are a helpful customer support assistant for Acme Corp."


def call_llm(prompt: str) -> str:
    """Pretend to be an LLM: just echo the prompt back.

    This lets us build and test the whole gateway for free.
    """
    return f"[mock LLM] You said: {prompt}"