from dotenv import load_dotenv
from langfuse import get_client

load_dotenv()

langfuse = get_client()

print("Langfuse client initialized")

with langfuse.start_as_current_observation(
    as_type="span",
    name="test-trace",
    input={
        "message": "Hello from my Personal AI Research Agent"
    },
) as span:

    span.update(
        output={
            "message": "Langfuse is working!"
        }
    )

langfuse.flush()

print("Trace sent to Langfuse!")