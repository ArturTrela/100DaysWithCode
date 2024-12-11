from openai import OpenAI
from sek import sekrety

GPT_API_KEY = sekrety["API_KEY_GPT"]
GPT_API_NAME = sekrety["API_NAME_GPT"]

# client = OpenAI()
# completion = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#         {"role": "user", "content": "write a haiku about ai"}
#     ]
# )

client = OpenAI()

response = client.images.generate(
    prompt="A cute baby sea otter",
    n=2,
    size="1024x1024"
)

print(response.data[0].url)