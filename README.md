# 🌍 Agentic Travel Companion

## 🚀 Project Overview

Agentic Travel Companion is an intelligent AI-powered Streamlit application that transforms travel planning into an interactive, personalized experience. Leveraging multiple specialized AI agents, this chatbot provides comprehensive travel assistance from destination selection to detailed trip planning.

## ✨ Key Features

- **Destination Weather Insights**: Real-time weather forecasting
- **Personalized Itinerary Planning**: Custom trip recommendations
- **Budget Estimation**: Tailored financial guidance
- **Culinary Exploration**: Local food and culture insights
- **Accommodation Suggestions**: Hotel and tourist spot recommendations

## 🤖 AI Agents Ecosystem

The application comprises five specialized agents:

1. **Weather Expert Agent**
   - Provides accurate weather forecasts
   - Retrieves real-time meteorological data

2. **Pre-Planning Agent**
   - Generates comprehensive travel itineraries
   - Offers packing tips and travel advice

3. **Budgeting Agent**
   - Estimates travel costs
   - Breaks down expenses for flights, hotels, and daily expenditures

4. **Food & Culture Agent**
   - Recommends local cuisines
   - Highlights cultural experiences and traditions

5. **Hotels & Places Agent**
   - Suggests accommodations
   - Identifies must-visit tourist attractions

## 🛠 Technology Stack

- **Framework**: Streamlit
- **AI Framework**: CrewAI
- **Large Language Model**: Mistral 7B
- **APIs**: 
  - Weather API
  - Geocoding API
- **Deployment**: Ollama for local LLM inference

## 📋 Prerequisites

- Python 3.8+
- Ollama
- Mistral LLM
- Weather API Credentials
- Geocoding API Credentials

## 🚀 Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/yourusername/agentic-travel-companion.git
cd agentic-travel-companion
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Create a .env file in the project root
WEATHER_API_URL=your_weather_api_url
GEO_API_URL=your_geocoding_api_url
```

## 🔧 Running the Application

```bash
streamlit run src/chatbot.py
```

## 🌐 Usage Workflow

1. Select destination country
2. View weather forecast
3. Generate trip itinerary
4. Estimate travel budget
5. Explore local cuisine
6. Get hotel and place recommendations

## 📈 Future Enhancements

- Multilingual support
- More advanced AI agent capabilities
- Enhanced personalization
- Integration with booking platforms

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

MIT License

## 🙏 Acknowledgements

- CrewAI
- Mistral AI
- Streamlit
- Ollama

**Happy Traveling! 🌍✈️**
