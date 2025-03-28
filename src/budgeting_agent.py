import yaml
from crewai import Agent
from utils import call_llm

class BudgetingAgent:
    def __init__(self):
        with open("agents/budgeting_agent.yml", "r") as file:
            config = yaml.safe_load(file)

        self.agent = Agent(
            name=config["name"],
            role=config["role"],
            goal=config["goal"],
            backstory=config["backstory"],
        )

    def estimate_budget(self, country, days, budget):
        """Estimate travel budget using LLM."""
        
        # Creating a detailed prompt for the LLM to calculate the estimated budget.
        prompt = (
            f"Estimate the total budget for a {days}-day trip to {country}. "
            f"The user has an estimated budget of ${budget} for the trip. "
            "Please include an estimate for flights, hotels, food, and local transport. "
            "Consider the country's general cost of living and provide a rough budget breakdown."
        )
        
        # Call LLM (Ollama or your preferred model) for budget estimation
        estimated_budget = call_llm(prompt)
        
        return estimated_budget
