from datetime import datetime
from typing import List
from pydantic import BaseModel
from google.adk.agents import LlmAgent

class FlightInfo(BaseModel):
    flight_number: str
    departure_time: str
    arrival_time: str
    airline: str
    price: float

class FlightSearchResult(BaseModel):
    flights: List[FlightInfo]

def get_date(phrase: str) -> str:
    """Convert a phrase like 'today' or 'tomorrow' to an actual date string."""
    today = datetime.now()
    if phrase.lower() == 'today':
        date = today.strftime('%Y-%m-%d')
    elif phrase.lower() == 'tomorrow':
        tomorrow = today.replace(day=today.day + 1)
        date = tomorrow.strftime('%Y-%m-%d')
    else:
        date = today.strftime('%Y-%m-%d')  # Default to today if phrase not recognized
    return date

def get_flights(date: str) -> FlightSearchResult:
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

# Create the flight agent with Google ADK
root_agent = LlmAgent(
    model="gemini-2.0-flash-exp",  # Using Gemini model
    name="flight_assistant",
    description="A helpful flight assistant that helps users find and book flights",
    instruction="""You are a helpful flight assistant that helps users find and book flights.
When a user asks about flights:
1. First, determine the date they want to travel using the get_date tool
2. Then, use the get_flights tool to search for available flights
3. Present the flight information in a clear, organized manner
4. Always confirm the date before searching for flights
5. If the user's request is unclear, ask for clarification
""",
    tools=[get_date, get_flights],
    input_schema=FlightSearchResult,
    output_key="flight_search_results"
)