import logging
from dataclasses import dataclass
from typing import List, Dict, Any

# Setup logging configuration
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@dataclass
class AgentResponse:
    data: List[Dict[str, Any]]
    reasoning: str

class POIAgent:
    def __init__(self, pois: List[Dict[str, Any]]):
        """
        Initialize the POIAgent with a list of points of interest (POIs).
        Each POI is expected to be a dictionary with keys including 'name', 'category', 'rating', and 'location'.
        """
        self.pois = pois
        logger.debug(f"POIAgent initialized with {len(pois)} POIs.")

    def search_pois(self, location: str, category: str, max_results: int = 5) -> AgentResponse:
        """
        Search for POIs by location and category, return up to max_results sorted by rating descending.

        Parameters:
        - location: The location to filter POIs.
        - category: The category to filter POIs.
        - max_results: Maximum number of POIs to return.

        Returns:
        - AgentResponse containing the filtered POIs and reasoning.
        """
        logger.debug(f"Searching POIs for location='{location}', category='{category}', max_results={max_results}")

        # Filter POIs by location and category
        filtered_pois = [
            poi for poi in self.pois
            if poi.get('location', '').lower() == location.lower()
            and poi.get('category', '').lower() == category.lower()
        ]
        logger.debug(f"Found {len(filtered_pois)} POIs matching location and category.")

        # Sort POIs by rating descending
        sorted_pois = sorted(filtered_pois, key=lambda x: x.get('rating', 0), reverse=True)
        logger.debug("POIs sorted by rating descending.")

        # Limit results to max_results
        limited_pois = sorted_pois[:max_results]
        logger.debug(f"Returning top {len(limited_pois)} POIs.")

        reasoning = (f"Searched for POIs in location '{location}' with category '{category}'. "
                     f"Found {len(filtered_pois)} matches, returning top {len(limited_pois)} by rating.")

        return AgentResponse(data=limited_pois, reasoning=reasoning)

# Example usage
if __name__ == "__main__":
    sample_pois = [
        {'name': 'Central Park', 'category': 'park', 'rating': 4.7, 'location': 'New York'},
        {'name': 'Metropolitan Museum of Art', 'category': 'museum', 'rating': 4.8, 'location': 'New York'},
        {'name': 'Statue of Liberty', 'category': 'monument', 'rating': 4.6, 'location': 'New York'},
        {'name': 'Brooklyn Bridge', 'category': 'monument', 'rating': 4.5, 'location': 'New York'},
        {'name': 'MoMA', 'category': 'museum', 'rating': 4.6, 'location': 'New York'},
        {'name': 'Golden Gate Park', 'category': 'park', 'rating': 4.7, 'location': 'San Francisco'},
        {'name': 'Alcatraz Island', 'category': 'monument', 'rating': 4.7, 'location': 'San Francisco'},
    ]

    agent = POIAgent(sample_pois)
    response = agent.search_pois(location="New York", category="museum", max_results=3)
    print("Agent Reasoning:", response.reasoning)
    print("POIs Found:")
    for poi in response.data:
        print(f" - {poi['name']} (Rating: {poi['rating']})")
