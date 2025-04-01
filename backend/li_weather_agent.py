from llama_index.llms.openai import OpenAI
from llama_index.core.agent.workflow import FunctionAgent
import asyncio
from llama_index.core.agent.workflow import ToolCallResult

from dotenv import load_dotenv
load_dotenv()

def multiply(a: float, b: float) -> float:
    """Multiply two numbers and returns the product"""
    return a * b


def add(a: float, b: float) -> float:
    """Add two numbers and returns the sum"""
    return a + b

llm = OpenAI(model="gpt-4o-mini")
agent = FunctionAgent(
    tools=[multiply, add],
    llm=llm,
    system_prompt="You are an agent that can perform basic mathematical operations using tools.",
)


async def run_agent_verbose(query: str):
    handler = agent.run(query)
    async for event in handler.stream_events():
        if isinstance(event, ToolCallResult):
            print(
                f"Called tool {event.tool_name} with args {event.tool_kwargs}\nGot result: {event.tool_output}"
            )

    return await handler

async def main():
    response = await run_agent_verbose("What is (121 + 2) * 5?")
    print(str(response))

if __name__ == "__main__":
    asyncio.run(main())