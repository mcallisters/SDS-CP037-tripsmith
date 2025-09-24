import logging
from typing import List, Dict, Any
from dataclasses import dataclass

# Set up logging for debugging and reasoning
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@dataclass
class AgentResponse:
    data: List[Dict[str, Any]]
    reasoning: str

class HotelAgent:
    def __init__(self):
        # Initialize the agent, could include API keys, config, etc.
        logger.debug("Initializing HotelAgent")

    def search_hotels(self, location: str, check_in: str, check_out: str, guests: int, max_results: int = 5) -> AgentResponse:
        """
        Search for hotels based on location, check-in/check-out dates, and number of guests.
        Returns an AgentResponse containing hotel data and the reasoning behind the search.
        """
        logger.debug(f"Starting hotel search for location={location}, check_in={check_in}, check_out={check_out}, guests={guests}, max_results={max_results}")

        # Reasoning: We want to find hotels in the specified location that can accommodate the number of guests,
        # available for the given dates, limiting the number of results to max_results.
        reasoning = (
            f"Searching for up to {max_results} hotels in {location} that can accommodate {guests} guests "
            f"from {check_in} to {check_out}."
        )
        logger.info(f"Reasoning: {reasoning}")

        # For demonstration, we use a static list of hotels. In a real implementation, this would query a database or API.
        hotels = [
            {"name": "Grand Plaza Hotel", "location": location, "max_guests": 2, "rating": 4.5, "available": True},
            {"name": "City Lights Inn", "location": location, "max_guests": 4, "rating": 4.0, "available": True},
            {"name": "Comfort Suites", "location": location, "max_guests": 3, "rating": 4.2, "available": False},
            {"name": "Luxury Stay", "location": location, "max_guests": 5, "rating": 4.8, "available": True},
            {"name": "Budget Inn", "location": location, "max_guests": 2, "rating": 3.8, "available": True},
            {"name": "Downtown Hotel", "location": location, "max_guests": 4, "rating": 4.3, "available": True},
        ]
        logger.debug(f"Initial hotel list: {hotels}")

        # Filter hotels that can accommodate the number of guests and are available
        filtered_hotels = [hotel for hotel in hotels if hotel["max_guests"] >= guests and hotel["available"]]
        logger.debug(f"Filtered hotels for guests >= {guests} and availability: {filtered_hotels}")

        # Sort by rating descending
        sorted_hotels = sorted(filtered_hotels, key=lambda x: x["rating"], reverse=True)
        logger.debug(f"Sorted hotels by rating: {sorted_hotels}")

        # Limit to max_results
        limited_hotels = sorted_hotels[:max_results]
        logger.debug(f"Limited hotels to max_results={max_results}: {limited_hotels}")

        return AgentResponse(data=limited_hotels, reasoning=reasoning)


# Example usage (can be removed or commented out in production)
if __name__ == "__main__":
    agent = HotelAgent()
    response = agent.search_hotels("New York", "2024-07-01", "2024-07-05", 3, 3)
    print("Reasoning:", response.reasoning)
    print("Hotels found:")
    for hotel in response.data:
        print(hotel)
