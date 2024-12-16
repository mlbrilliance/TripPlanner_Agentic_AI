from typing import List
from datetime import datetime
from pydantic import BaseModel

class Location(BaseModel):
    """Represents a geographical location.
    
    Attributes:
        name: Name of the location (e.g., city name)
        latitude: Latitude coordinate
        longitude: Longitude coordinate
    """
    name: str
    latitude: float
    longitude: float

class TripRequest(BaseModel):
    """Represents a trip request with all necessary details.
    
    Attributes:
        origin: Starting location
        destinations: List of destination locations
        start_date: Trip start date
        end_date: Trip end date
        budget: Total trip budget in USD
        interests: List of traveler's interests
    """
    origin: Location
    destinations: List[Location]
    start_date: datetime
    end_date: datetime
    budget: float
    interests: List[str]

class TripItinerary(BaseModel):
    """Represents a complete trip itinerary.
    
    Attributes:
        trip_request: Original trip request
        flights: Flight recommendations
        weather_forecasts: Weather information
        attractions: Suggested attractions and activities
    """
    trip_request: TripRequest
    flights: dict
    weather_forecasts: dict
    attractions: dict