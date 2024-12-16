# src/travel_planner/main.py
from typing import Any
from datetime import datetime
from dotenv import load_dotenv
from .models.trip import TripRequest, Location
from .agents.manager_agent import TripPlannerManager

def main() -> Any:
    """
    Main entry point for the travel planner application.
    
    Returns:
        Any: The generated trip itinerary
    """
    load_dotenv()
    
    # Create a sample trip request with correct Location initialization
    trip_request = TripRequest(
        origin=Location(
            name="New York",
            country="USA"
        ),
        destinations=[
            Location(
                name="Paris",
                country="France"
            ),
            Location(
                name="Rome",
                country="Italy"
            )
        ],
        start_date=datetime.strptime("2024-03-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2024-03-10", "%Y-%m-%d")
    )
    
    # Initialize and run the manager
    manager = TripPlannerManager()
    itinerary = manager.create_itinerary(trip_request)
    
    print("Trip Itinerary Generated:")
    print(f"From: {itinerary.trip_request.origin.name}")
    print(f"To: {[d.name for d in itinerary.trip_request.destinations]}")
    
    return itinerary

if __name__ == "__main__":
    main()