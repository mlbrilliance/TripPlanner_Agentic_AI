import os
from typing import List
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain.llms import Ollama
from ..models.trip import TripRequest, TripItinerary

class TripPlannerManager:
    """Manages the trip planning process using CrewAI agents."""

    def __init__(self) -> None:
        """Initialize the TripPlannerManager with required agents."""
        try:
            # Initialize Ollama LLM with only supported parameters
            llm = Ollama(
                model="llama2",
                temperature=0.7,
                base_url="http://127.0.0.1:11434",
                timeout=1200
            )
            
            # Test the connection
            try:
                llm("test")  # Simple test call
                print("Successfully connected to Ollama")
            except Exception as e:
                print(f"Error testing Ollama connection: {str(e)}")
                raise
            
            self.flight_agent = Agent(
                role='Flight Search Specialist',
                goal='Find the best flight options for travelers',
                backstory="""You are an expert in finding optimal flight routes and deals. 
                You consider factors like price, duration, layovers, and airline reputation.""",
                verbose=True,
                allow_delegation=False,
                llm=llm,
                tools=[]
            )

            self.weather_agent = Agent(
                role='Weather Analyst',
                goal='Provide accurate weather forecasts and recommendations',
                backstory="""You are a meteorologist specialized in travel weather forecasting.
                You analyze weather patterns and provide practical advice for travelers.""",
                verbose=True,
                allow_delegation=False,
                llm=llm,
                tools=[]
            )

            self.attraction_agent = Agent(
                role='Local Attractions Expert',
                goal='Recommend personalized attractions and activities',
                backstory="""You are a knowledgeable travel guide with extensive experience.
                You provide customized recommendations based on interests, budget, and weather.""",
                verbose=True,
                allow_delegation=False,
                llm=llm,
                tools=[]
            )

        except Exception as e:
            print(f"Error initializing TripPlannerManager: {str(e)}")
            raise

    def create_itinerary(self, trip_request: TripRequest) -> TripItinerary:
        """
        Create a complete trip itinerary using the specialized agents.

        Args:
            trip_request: The trip request containing all necessary details

        Returns:
            TripItinerary: A complete itinerary with flights, weather, and attractions
        """
        try:
            # Create tasks for each agent
            flight_task = Task(
                description=f"""Find flight options from {trip_request.origin.name} to 
                {trip_request.destinations[0].name} for dates {trip_request.start_date.date()} to 
                {trip_request.end_date.date()}. Consider a budget of ${trip_request.budget:.2f}.
                Provide detailed flight options including prices, times, and airlines.""",
                agent=self.flight_agent,
                expected_output="Detailed flight recommendations including prices, times, and airlines."
            )

            weather_task = Task(
                description=f"""Analyze weather patterns and provide forecast for 
                {trip_request.destinations[0].name} during {trip_request.start_date.date()} to 
                {trip_request.end_date.date()}. Include temperature ranges, precipitation chances,
                and practical packing recommendations.""",
                agent=self.weather_agent,
                expected_output="Detailed weather forecast with temperatures, conditions, and packing advice."
            )

            attraction_task = Task(
                description=f"""Recommend attractions and activities in {trip_request.destinations[0].name}
                based on interests: {', '.join(trip_request.interests)}. Consider weather forecast and
                a budget of ${trip_request.budget:.2f}. Provide detailed daily itinerary suggestions.""",
                agent=self.attraction_agent,
                expected_output="Detailed daily itinerary with attractions, activities, and costs."
            )

            # Create and run the crew
            crew = Crew(
                agents=[self.flight_agent, self.weather_agent, self.attraction_agent],
                tasks=[flight_task, weather_task, attraction_task],
                verbose=2,
                process=Process.sequential
            )

            # Get the results
            results = crew.kickoff()

            # Parse and structure the results
            return TripItinerary(
                trip_request=trip_request,
                flights={"recommendations": results[0]},
                weather_forecasts={"forecast": results[1]},
                attractions={"suggestions": results[2]}
            )
        except Exception as e:
            print(f"Error creating itinerary: {str(e)}")
            raise 