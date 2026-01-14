from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.core.config import settings


llmController = APIRouter()


async def get_openai_generator(query: str):
    from openai import OpenAI

    client = OpenAI(api_key=settings.deepseek_api_key, base_url=settings.deepseek_api_url)

    response = client.chat.completions.create(
        model=settings.deepseek_default_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": query},
        ],
        stream=True,
    )

    for chunk in response:
        yield chunk.choices[0].delta.content


@llmController.get("/deepseek/stream")
async def chat_with_model(query: str):
    return StreamingResponse(get_openai_generator(query), media_type="text/event-stream")


@llmController.get("/deepseek/chat")
async def chat_with_model(query: str):
    from openai import OpenAI

    print("Deepseek API URL:", settings.deepseek_api_url)
    print("Deepseek API Key:", settings.deepseek_api_key)
    print("Deepseek Models:", settings.deepseek_default_model)

    client = OpenAI(api_key=settings.deepseek_api_key, base_url=settings.deepseek_api_url)

    response = client.chat.completions.create(
        model=settings.deepseek_default_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": query},
        ],
        stream=True,
    )

    result = response.choices[0].message.content

    return {"data": result}
