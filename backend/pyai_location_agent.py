from pydantic import BaseModel

from pydantic_ai import Agent
from devtools import debug

class CityLocation(BaseModel):
    city: str
    country: str


agent = Agent('openai:gpt-4o', result_type=CityLocation)
result = agent.run_sync('Where were the olympics held in 2012?')
debug(result.all_messages())
print(result.data)
#> city='London' country='United Kingdom'

print(result.usage())
"""
Usage(requests=1, request_tokens=57, response_tokens=8, total_tokens=65, details=None)
"""