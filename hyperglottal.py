"""Glyphic protocol stubs (Hyper/QuantaGlottal)."""
import hashlib

def encode(message: str) -> str:
    h = hashlib.md5(message.encode()).hexdigest()[:8]
    return f"⟦{h}:{len(message)}⟧"

def evolve(seed: str) -> str:
    return f"v{int(hashlib.sha1(seed.encode()).hexdigest()[:4],16)%9999:04d}"
