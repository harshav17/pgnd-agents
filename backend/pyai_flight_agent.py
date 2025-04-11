from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel

from pydantic_ai import Agent, RunContext
from pydantic_ai.tools import ToolDefinition
from devtools import debug

class FlightInfo(BaseModel):
    flight_number: str
    departure_time: str
    arrival_time: str
    airline: str
    price: float

class FlightSearchResult(BaseModel):
    flights: List[FlightInfo]

class FlightAgentDeps(BaseModel):
    selected_date: Optional[str] = None

agent = Agent(
    'openai:gpt-4o',
    result_type=FlightSearchResult,
    deps_type=FlightAgentDeps
)

@agent.tool
def get_date(ctx: RunContext[FlightAgentDeps], phrase: str) -> str:
    """Convert a phrase like 'today' or 'tomorrow' to an actual date string."""
    today = datetime.now()
    if phrase.lower() == 'today':
        date = today.strftime('%Y-%m-%d')
    elif phrase.lower() == 'tomorrow':
        tomorrow = today.replace(day=today.day + 1)
        date = tomorrow.strftime('%Y-%m-%d')
    else:
        date = today.strftime('%Y-%m-%d')  # Default to today if phrase not recognized
    
    # Update the dependencies with the selected date
    ctx.deps.selected_date = date
    return date

async def prepare_get_flights(ctx: RunContext[FlightAgentDeps], tool_def: ToolDefinition) -> Union[ToolDefinition, None]:
    """Prepare function to ensure getDate is called before getFlights."""
    if ctx.deps.selected_date is not None:
        return tool_def  # Allow getFlights to be called if date is selected
    return None  # Don't allow getFlights to be called if date isn't selected

@agent.tool(prepare=prepare_get_flights)
def get_flights(ctx: RunContext[FlightAgentDeps], date: str) -> FlightSearchResult:
    """Get flight information for a given date."""
    # This is a mock implementation. In a real scenario, this would call an actual flight API
    mock_flights = [
        FlightInfo(
            flight_number="AA123",
            departure_time="08:00",
            arrival_time="10:30",
            airline="American Airlines",
            price=299.99
        ),
        FlightInfo(
            flight_number="DL456",
            departure_time="14:00",
            arrival_time="16:30",
            airline="Delta Airlines",
            price=349.99
        )
    ]
    return FlightSearchResult(flights=mock_flights)

if __name__ == "__main__":
    result = agent.run_sync("Find me flights for tomorrow", deps=FlightAgentDeps())
    debug(result.all_messages())
    print(result.data)
    print(result.usage()) 