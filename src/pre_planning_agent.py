import yaml
from crewai import Agent
from utils import call_llm 

class PrePlanningAgent:
    def __init__(self):
        with open("agents/pre_planning_agent.yml", "r") as file:
            config = yaml.safe_load(file)

        self.agent = Agent(
            name=config["name"],
            role=config["role"],
            goal=config["goal"],
            backstory=config["backstory"],
        )

    def generate_plan(self, country, days, weather_info):
        """Generate a travel plan using LLM."""
        prompt = (
            f"Generate a detailed travel plan for a {days}-day trip to {country}. "
            f"Include packing suggestions based on weather conditions: {weather_info}. "
            "Provide essential travel tips for a smooth experience "
            "Also suggest famous places to visit and make a tentative plan for 2-3 days in each location."
        )
        return call_llm(prompt)

