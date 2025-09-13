"""EthicChain active guard — veto on policy breach (demo)."""
POLICY = {'care': True, 'vigilance': True, 'public_good': True}

def veto(risk: str) -> bool:
    return risk in {'harm_human','illegal','privacy_breach'}
