from atlas.core.config import AI_PROVIDER

if AI_PROVIDER == "ollama":
    from atlas.ai.ollama import ask

elif AI_PROVIDER == "openrouter":
    from atlas.ai.openrouter import ask

else:
    raise ValueError(f"Неизвестный AI_PROVIDER: {AI_PROVIDER}")