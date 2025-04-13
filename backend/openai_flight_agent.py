from datetime import datetime
from typing import List
from pydantic import BaseModel

from agents import Agent, Runner, function_tool

class FlightInfo(BaseModel):
    flight_number: str
    departure_time: str
    arrival_time: str
    airline: str
    price: float

class FlightSearchResult(BaseModel):
    flights: List[FlightInfo]

@function_tool
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

@function_tool
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

# Create the flight agent with appropriate instructions and tools
flight_agent = Agent(
    name="Flight Assistant",
    instructions="You are a helpful flight assistant that helps users find and book flights. "
                "You can search for flights and provide detailed information about available options. "
                "Always confirm the date before searching for flights. "
                "Your response must be a valid FlightSearchResult object with a list of flights.",
    tools=[get_date, get_flights],
    output_type=FlightSearchResult
)

async def main():
    # Example usage
    result = await Runner.run(
        flight_agent,
        input="Find me flights for tomorrow from New York to Los Angeles"
    )
    if isinstance(result.final_output, FlightSearchResult):
        print("Found flights:")
        for flight in result.final_output.flights:
            print(f"Flight {flight.flight_number} ({flight.airline}):")
            print(f"  Departure: {flight.departure_time}")
            print(f"  Arrival: {flight.arrival_time}")
            print(f"  Price: ${flight.price}")
    else:
        print("Error: Unexpected output type")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()) 