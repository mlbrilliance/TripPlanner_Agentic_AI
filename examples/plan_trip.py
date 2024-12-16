import os
from datetime import datetime
from dotenv import load_dotenv
from travel_planner.models.trip import Location, TripRequest
from travel_planner.agents.manager_agent import TripPlannerManager

def get_date_input(prompt: str) -> datetime:
    """Get a valid date input from the user."""
    while True:
        try:
            date_str = input(prompt + " (YYYY-MM-DD): ")
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")

def get_float_input(prompt: str) -> float:
    """Get a valid float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number")

def get_location_input(prompt: str) -> Location:
    """Get location details from the user."""
    print(f"\n{prompt}")
    name = input("Enter city name: ")
    lat = get_float_input("Enter latitude: ")
    lon = get_float_input("Enter longitude: ")
    return Location(name=name, latitude=lat, longitude=lon)

def get_interests() -> list[str]:
    """Get user interests for the trip."""
    print("\nEnter your interests (comma-separated)")
    print("Examples: art, food, history, nature, shopping, music, sports")
    interests_input = input("Interests: ")
    return [interest.strip() for interest in interests_input.split(",")]

def main() -> None:
    """Run the trip planner with user inputs."""
    print("Welcome to the AI Trip Planner!")
    print("--------------------------------")

    # Get trip details from user
    origin = get_location_input("Enter origin location details:")
    destination = get_location_input("Enter destination location details:")
    
    start_date = get_date_input("\nEnter start date")
    end_date = get_date_input("Enter end date")
    
    budget = get_float_input("\nEnter your budget in USD: ")
    interests = get_interests()

    # Create trip request
    trip_request = TripRequest(
        origin=origin,
        destinations=[destination],
        start_date=start_date,
        end_date=end_date,
        budget=budget,
        interests=interests
    )

    print("\nPlanning your trip...")
    print("----------------------")

    # Create trip planner and generate itinerary
    planner = TripPlannerManager()
    itinerary = planner.create_itinerary(trip_request)
    
    # Print results
    print("\nTrip Itinerary:")
    print("===============")
    print(f"From: {itinerary.trip_request.origin.name}")
    print(f"To: {[d.name for d in itinerary.trip_request.destinations]}")
    print(f"Dates: {itinerary.trip_request.start_date.date()} - {itinerary.trip_request.end_date.date()}")
    print(f"Budget: ${itinerary.trip_request.budget:,.2f}")
    print(f"Interests: {', '.join(itinerary.trip_request.interests)}")
    print("\nFlights:", itinerary.flights)
    print("\nWeather:", itinerary.weather_forecasts)
    print("\nAttractions:", itinerary.attractions)

if __name__ == "__main__":
    main()