"""Fractal memory (ZDM) — short/long/latent/absence_active (demo)."""
from typing import Dict, Any

class ZDM:
    def __init__(self):
        self.short = {}
        self.long = {}
        self.latent = {}
        self.absent = {}

    def remember(self, k: str, v: Any, layer: str = 'short'):
        getattr(self, layer)[k] = v

    def recall(self, k: str):
        for layer in ('short','long','latent','absent'):
            if k in getattr(self, layer):
                return getattr(self, layer)[k]
        return None
