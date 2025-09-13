"""Multi-agent orchestration skeleton (demo)."""
from typing import List, Callable

def vote(agents: List[Callable[[str], str]], prompt: str) -> str:
    outputs = [a(prompt) for a in agents]
    # simple majority on shortest output (low-token bias)
    outputs.sort(key=len)
    return outputs[0]
