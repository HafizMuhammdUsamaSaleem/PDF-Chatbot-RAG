# Smart Tour Planner 🤖🌍

Welcome to **Smart Tour Planner**, an AI-powered chatbot designed to make your travel planning easy, interactive, and fun! With just a few clicks, you’ll get personalized travel advice, including weather updates, budgeting tips, food recommendations, cultural insights, and hotel suggestions for your trip.

## Features

- **Weather Forecast**: Get real-time weather updates for your chosen destination.
- **Pre-Planning**: Receive travel tips, packing suggestions, and essential recommendations for your destination.
- **Budgeting**: Estimate your total travel budget based on your destination and duration of stay.
- **Food & Culture**: Discover famous local dishes and learn about the rich cultural heritage of the country.
- **Hotel & Places**: Find the best hotels and top places to visit for an unforgettable experience.
- **Interactive Chatbot**: A friendly AI assistant that helps you plan your trip step by step.

## Technologies Used

- **Streamlit**: Building the interactive chatbot interface.
- **Mistral 7B LLM**: Using a large language model to generate responses and travel recommendations.
- **Weather API**: Fetching live weather data for your selected country.

## How It Works

**Follow these steps to plan your trip using the Smart Tour Planner chatbot**:

1. **Enter Your Destination**  
   The chatbot will ask you to enter the **country** you want to visit.  
   After submission, it will provide you with the **current weather** update for your chosen country.

2. **Pre-Planning**  
   The chatbot will ask if you would like to pre-plan your trip. If you choose **Yes**, it will then ask **how many days** you plan to stay.  
   Based on the number of days, it will give you **packing suggestions**, **travel tips**, and **pre-travel recommendations** for the destination.

3. **Budgeting**  
   You will then be asked for your **estimated budget** for the trip (in USD).  
   The chatbot will calculate the budget based on your **country**, **number of days**, and provide you with an estimate covering **flights, hotels, food**, and **local transport**.

4. **Food & Culture**  
   Next, the chatbot will ask if you'd like to know about **delicious local foods** and **cultural heritage**.  
   It will provide you with recommendations about the top **local dishes** and insights into the **cultural experiences** of the country.

5. **Hotels & Places to Visit**  
   Finally, the chatbot will suggest the **best hotels** and **places to visit** in your selected country.  
   You’ll get recommendations for luxurious hotels, hidden gems, and top tourist attractions.

6. **Completion**  
   After all steps, the chatbot will display a **success message** confirming that your travel plan is ready! You can then proceed with your trip, and if you want to plan another one, simply refresh the page to start over.

## LLM Model

We are using **Mistral 7B**, a large language model, to power the conversational aspect of the app and generate travel recommendations. The model provides accurate and rich insights throughout the entire planning process.

In future updates, we plan to experiment with lower-parameter models to check efficiency and performance, ensuring that the chatbot remains fast and responsive.

## Installation

To run **Smart Tour Planner** on your local machine:

1. Clone the repository:
   
   ```bash
   git clone https://github.com/your-username/smart-tour-planner.git
   cd smart-tour-planner
2. Create a virtual environment:
    ```bash
    python -m venv venv
3. Activate the virtual environment:
4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
5. Create a .env file for API keys (necessary for weather)