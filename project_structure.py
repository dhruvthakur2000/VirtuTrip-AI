import os
from pathlib import Path


DIRECTORIES = [
    "src/agents",
    "src/rag",
    "src/graphs",
    "src/utils",
    "data/destinations",
    "data/chroma_db",
    "tests",
    "logs"
]

INIT_FILES = [
    "src/__init__.py",
    "src/agents/__init__.py",
    "src/rag/__init__.py",
    "src/graphs/__init__.py",
    "src/utils/__init__.py",
]

GITKEEP_FILES = [
    "data/destinations/.gitkeep",
    "data/chroma_db/.gitkeep",
    "logs/.gitkeep"
]

PYTHON_PLACEHOLDERS = {
    "src/agents/planner_agent.py": "PlannerAgent - Trip planning and validation",
    "src/agents/explorer_agent.py": "ExplorerAgent - Attraction and activity discovery",
    "src/agents/budget_agent.py": "BudgetAgent - Budget handling",
    "src/agents/booking_agent.py": "BookingAgent - Booking suggestions",
    "src/agents/itinerary_agent.py": "ItineraryAgent - Itinerary generation",
    "src/rag/embeddings.py": "Embedding generator",
    "src/rag/vector_store.py": "ChromaDB vector store",
    "src/rag/retriever.py": "RAG retrieval engine",
    "src/graphs/workflow.py": "LangGraph workflow",
    "src/utils/config.py": "Config utilities",
    "src/utils/logger.py": "Logging utilities",
    "src/utils/api_clients.py": "External API clients",
    "src/app.py": "Streamlit entrypoint",
    "tests/test_agents.py": "Agent unit tests",
}

CONFIG_FILES = [
    "requirements.txt",
    ".env.example",
    "setup.py",
    "Dockerfile",
    "docker-compose.yml",
    ".gitignore",
    ".dockerignore"
]

DOC_FILES = [
    "README.md",
    "QUICKSTART.md",
    "ARCHITECTURE.md",
    "PROJECT_SUMMARY.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md"
]

def make_dirs(base, dirs):
    for d in dirs:
        path = os.path.join(base, d)
        os.makedirs(path, exist_ok=True)
        print("Created:", path)

def make_files(base, files):
    for f in files:
        path = os.path.join(base, f)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "a").close()
        print("Created:", path)

def create_structure():
    root = "."
    print("\nCreating VirtuTrip-AI project structure...\n")

    make_dirs(root, DIRECTORIES)
    make_files(root, INIT_FILES)
    make_files(root, GITKEEP_FILES)
    make_files(root, PYTHON_PLACEHOLDERS)
    make_files(root, CONFIG_FILES)
    make_files(root, DOC_FILES)

    print("\nVirtuTrip-AI project structure completed!")

if __name__ == "__main__":
    create_structure()