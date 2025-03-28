import yaml
from crewai import Agent
from utils import call_llm

class FoodCultureAgent:
    def __init__(self):
        with open("agents/food_culture_agent.yml", "r") as file:
            config = yaml.safe_load(file)

        self.agent = Agent(
            name=config["name"],
            role=config["role"],
            goal=config["goal"],
            backstory=config["backstory"],
        )

    def recommend_food_and_culture(self, country):
        """Get food and cultural highlights using LLM."""
        prompt = (
            f"Suggest the best local dishes and cultural experiences for a traveler in {country}. "
            "Include food specialties, festivals, and traditions."
        )
        return call_llm(prompt)
