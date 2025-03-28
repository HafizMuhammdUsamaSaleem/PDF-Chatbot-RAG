import streamlit as st
from weather_agent import WeatherAgent
from pre_planning_agent import PrePlanningAgent
from budgeting_agent import BudgetingAgent
from food_culture_agent import FoodCultureAgent
from hotels_places_agent import HotelsPlacesAgent

class TourGuideChatbot:
    def __init__(self):
        self.weather_agent = WeatherAgent()
        self.pre_planning_agent = PrePlanningAgent()
        self.budgeting_agent = BudgetingAgent()
        self.food_agent = FoodCultureAgent()
        self.hotels_agent = HotelsPlacesAgent()

    def run(self):
        st.title("🌍 Tour Guide Chatbot")
        st.write("Welcome! I’m here to help you plan your trip. Let’s get started! 🚀")

        # Initialize session state
        if "messages" not in st.session_state:
            st.session_state.messages = []
        if "step" not in st.session_state:
            st.session_state.step = 1
        if "country" not in st.session_state:
            st.session_state.country = None
        if "days" not in st.session_state:
            st.session_state.days = None
        if "weather_info" not in st.session_state:
            st.session_state.weather_info = None
        if "budget" not in st.session_state:
            st.session_state.budget = None
        if "food_preferences" not in st.session_state:
            st.session_state.food_preferences = None
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
        if st.session_state.step == 1:
            country = st.text_input("✈️ Where would you like to go?")
            if st.button("Submit Country"):
                st.session_state.country = country
                st.session_state.messages.append({"role": "user", "content": f"🌍 I'm planning a trip to **{country}**!"})
                weather_info = self.weather_agent.get_weather(country)
                st.session_state.weather_info = weather_info
                st.session_state.messages.append({"role": "assistant", "content": f"🌦️ {weather_info}."})
                st.session_state.step = 2
                st.rerun()
        if st.session_state.step == 2:
            if st.button("Can I help you plan your trip?"):
                st.session_state.messages.append({"role": "assistant", "content": "🗓️ How many days will you stay?"})
                st.session_state.step = 3
                st.rerun()
        if st.session_state.step == 3:
            days = st.number_input("🗓️ How many days do you plan to stay?", min_value=1, max_value=365, step=1)
            if st.button("Set Number of Days"):
                st.session_state.days = days
                pre_plan_info = self.pre_planning_agent.generate_plan(st.session_state.country, st.session_state.days, st.session_state.weather_info)
                st.write(f"🗺️ Here’s a suggested itinerary for your {days}-day trip to **{st.session_state.country}**: ")
                st.write(pre_plan_info)

                st.session_state.messages.append({"role": "user", "content": f"🗓️ I plan to stay for **{days} days**."})
                st.session_state.messages.append({"role": "assistant", "content": pre_plan_info})
                st.session_state.step = 4
                st.rerun()

        if st.session_state.step == 4:
            budget = st.number_input("💰 What’s your estimated budget for the trip? (in USD)", min_value=100, step=50)
            if st.button("Calculate My Budget"):
                st.session_state.budget = budget
                budget_info = self.budgeting_agent.estimate_budget(st.session_state.country, st.session_state.days, budget)
                st.session_state.messages.append({"role": "user", "content": f"💰 My estimated budget is **${budget}**."})
                st.session_state.messages.append({"role": "assistant", "content": budget_info})
                st.session_state.step = 5
                st.rerun()

        if st.session_state.step == 5:
            # food_preferences = st.text_input("🍽️ Do you have any dietary preferences? (Vegetarian, Halal, etc.)")
            # if st.button("Suggest Local Cuisine"):
            if st.button(f"🍽️ Discover the Delicious Flavors and Rich Culture of **{st.session_state.country}**! 🌍🍴"):
                # st.session_state.food_preferences = food_preferences
                food_info = self.food_agent.recommend_food_and_culture(st.session_state.country)
                # st.session_state.messages.append({"role": "user", "content": f"🍽️ I prefer **{food_preferences}** food."})
                st.session_state.messages.append({"role": "assistant", "content": f"🍽️ Here's what you can try in **{st.session_state.country}**: {food_info}"})
                st.session_state.step = 6
                st.rerun()

        if st.session_state.step == 6:
            if st.button("🏨 Suggest the best hotels & places to visit"):
                hotels_info = self.hotels_agent.recommend_hotels_and_places(st.session_state.country)
                st.session_state.messages.append({"role": "assistant", "content": f"🏨 Top hotels and places to visit in **{st.session_state.country}**: {hotels_info}"})
                st.session_state.step = 7
                st.rerun() 
        if st.session_state.step == 7:
            st.success("✅ Your travel plan is ready! Enjoy your trip! 🎉")
            st.write("You have completed your travel plan. If you'd like to start over, simply refresh the page.")


if __name__ == "__main__":
    chatbot = TourGuideChatbot()
    chatbot.run()
