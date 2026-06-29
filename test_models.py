from openai import OpenAI
from atlas.core.config import OPENROUTER_API_KEY

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

models = client.models.list()

print(f"Найдено моделей: {len(models.data)}")
print()

for model in models.data[:30]:
    print(model.id)