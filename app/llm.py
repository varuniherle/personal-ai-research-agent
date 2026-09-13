import os

from dotenv import load_dotenv
from groq import Groq
from langfuse import get_client

load_dotenv()

groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

langfuse = get_client()


def ask_llm(prompt: str) -> str:

    with langfuse.start_as_current_observation(
        as_type="generation",
        name="groq-chat",
        model="openai/gpt-oss-120b",
        input=prompt,
    ) as generation:

        response = groq_client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        answer = response.choices[0].message.content

        generation.update(
            output=answer,
            usage_details={
                "input": response.usage.prompt_tokens,
                "output": response.usage.completion_tokens,
                "total": response.usage.total_tokens,
            },
        )

    langfuse.flush()

    return answer