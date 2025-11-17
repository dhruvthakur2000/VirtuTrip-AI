
# Contributing to VirtuTrip-AI

Thank you for your interest in contributing to VirtuTrip-AI! Here's how you can help:

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/virtutrip-ai.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Set up development environment (see README.md)

## Development Guidelines

### Code Style

- Follow PEP 8 style guide
- Use Black for code formatting: `black src/`
- Run flake8 for linting: `flake8 src/`
- Use type hints where applicable

### Testing

- Write tests for new features
- Ensure all tests pass: `pytest tests/ -v`
- Maintain test coverage above 80%

### Commit Messages

Use conventional commits format:
```
feat: add new budget calculation feature
fix: resolve ChromaDB connection issue
docs: update README with deployment instructions
test: add tests for ExplorerAgent
refactor: improve error handling in API clients
```

### Pull Request Process

1. Update documentation if needed
2. Add tests for new features
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Submit PR with clear description

## Areas for Contribution

### High Priority
- Additional API integrations (Booking.com, Skyscanner)
- Multi-language support
- Mobile-responsive UI improvements
- Performance optimizations

### Good First Issues
- Add more seed data to vector store
- Improve error messages
- Add more test coverage
- Documentation improvements

### Enhancement Ideas
- User authentication
- Trip sharing features
- Collaborative planning
- Budget tracking
- Real booking integration

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Report issues professionally

## Questions?

Open an issue or start a discussion on GitHub!
