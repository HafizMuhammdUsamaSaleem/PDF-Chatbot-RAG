import yaml
from crewai import Agent
from utils import call_llm

class HotelsPlacesAgent:
    def __init__(self):
        with open("agents/hotels_places_agent.yml", "r") as file:
            config = yaml.safe_load(file)

        self.agent = Agent(
            name=config["name"],
            role=config["role"],
            goal=config["goal"],
            backstory=config["backstory"],
        )

    def recommend_hotels_and_places(self, country):
        """Provide hotel and sightseeing recommendations using LLM."""
        prompt = (
            f"Suggest the best hotels and tourist attractions in {country}. "
            "Provide budget, mid-range, and luxury options for hotels."
        )
        return call_llm(prompt)
