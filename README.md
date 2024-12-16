# TripPlanner - Agentic AI - Crew AI

A sophisticated trip planning system built using the Crew AI Agentic Framework. This project leverages AI agents to create personalized travel itineraries, handle accommodation bookings, and suggest activities based on user preferences.

## Features
- Developer: Nick Sudh
-LinkedIn: https://www.linkedin.com/in/nick-sudh/

## Features

- Personalized travel itinerary generation
- Intelligent destination recommendations
- Activity and point of interest suggestions
- Accommodation booking assistance
- Budget optimization
- Weather-aware planning
- Multi-city trip coordination

## Dependencies

- Python 3.9+
- crewai
- langchain
- openai
- python-dotenv
- requests
- pydantic

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/TripPlanner_Agentic_AI.git
cd TripPlanner_Agentic_AI
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies using uv:
```bash
pip install uv
uv pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root:
```bash
OPENAI_API_KEY=your_openai_api_key
WEATHER_API_KEY=your_weather_api_key
```

2. Replace the API keys with your actual keys from:
- OpenAI: https://platform.openai.com/
- Weather API (optional): Your preferred weather service

## Usage

1. Run the trip planner:
```bash
python src/main.py
```

2. Follow the interactive prompts to:
- Enter your travel dates
- Specify destinations
- Set your budget
- Define preferences
- Review and confirm your itinerary

## Development Setup

1. Install development dependencies:
```bash
uv pip install -r requirements-dev.txt
```

2. Install pre-commit hooks:
```bash
pre-commit install
```

3. Run code quality tools:
```bash
ruff check .
ruff format .
```

## Testing

Run the test suite:
```bash
pytest tests/
```

For test coverage:
```bash
pytest --cov=src tests/
```

## Project Structure

```
TripPlanner_Agentic_AI/
├── src/
│   ├── agents/
│   ├── models/
│   ├── services/
│   └── utils/
├── tests/
├── docs/
├── .env
├── requirements.txt
└── requirements-dev.txt
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Crew AI Framework
- OpenAI
- All contributors and maintainers
