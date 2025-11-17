# VirtuTrip-AI: AI Virtual Tour Assistant

A production-ready multi-agent AI system for intelligent travel planning using LangGraph, ChromaDB, and real-time APIs.

## 🌟 Features

- **Multi-Agent Architecture**: Collaborative agents (Planner, Explorer, Budget, Booking, Itinerary)
- **RAG Pipeline**: Real-time retrieval from ChromaDB + external APIs
- **Real API Integration**: Google Places, OpenWeatherMap, ExchangeRate-API, REST Countries
- **LangGraph Orchestration**: State-based agent workflow
- **Streamlit UI**: Interactive, user-friendly interface
- **Production-Ready**: Logging, error handling, modular design

## 📁 Project Structure

```
VirtuTrip-AI/
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── planner_agent.py      # Trip planning logic
│   │   ├── explorer_agent.py     # Destination exploration
│   │   ├── budget_agent.py       # Budget calculation
│   │   ├── booking_agent.py      # Booking recommendations
│   │   └── itinerary_agent.py    # Itinerary generation
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── vector_store.py       # ChromaDB management
│   │   ├── retriever.py          # RAG retrieval logic
│   │   └── embeddings.py         # Embedding generation
│   ├── graphs/
│   │   ├── __init__.py
│   │   └── workflow.py           # LangGraph workflow
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── api_clients.py        # External API clients
│   │   ├── logger.py             # Logging configuration
│   │   └── config.py             # Configuration management
│   └── app.py                     # Streamlit application
├── data/
│   ├── destinations/              # Destination data
│   └── chroma_db/                 # ChromaDB storage
├── tests/
│   └── test_agents.py
├── .env.example
├── requirements.txt
├── setup.py
└── README.md
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

MIT License - see LICENSE file

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- LangGraph team for agent orchestration framework
- ChromaDB for vector database
- Streamlit for rapid UI development