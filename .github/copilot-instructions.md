# GitHub Copilot Instructions for MCP-B

## CRITICAL: MCP Server Usage

### Always Use Serena First (#serena)
For ALL code analysis, investigation, and understanding tasks, use Serena semantic tools:
- Symbol search (classes, functions, variables)
- Usage/reference analysis
- Semantic-enabled refactoring
- Project structure overview

### Use Context7 for Documentation (#context7)
For code generation, setup steps, or library/API documentation:
- Up-to-date API references
- Version-specific documentation
- Best practice patterns

## Project Overview

MCP-B (Master Client Bridge) is a Python package that provides:
- **MCP-B Protocol**: 4-layer encoding for agent-to-agent messaging
- **AMUM**: Progressive 3→6→9 human-AI alignment workflow
- **QCI**: Quantum coherence state tracking
- **ETHIC**: AI ethics principles enforcement

## Specialized Agent Roles

This project uses specialized Copilot agents for different tasks in the ML/AI pipeline:

### 🔬 Data Collector Agent
- **Role**: Gather and ingest data from various sources
- **Tools**: `#serena` for code analysis, `#context7` for API docs
- **Focus**: Data sources, APIs, scraping patterns, data validation

### 🧹 Data Prep Agent
- **Role**: Clean, transform, and prepare data for training
- **Tools**: pandas, numpy, data validation libraries
- **Focus**: Missing values, normalization, feature engineering, data quality

### 🤖 Model Trainer Agent
- **Role**: Design, train, and optimize ML models
- **Tools**: scikit-learn, pytorch, tensorflow, hyperparameter tuning
- **Focus**: Model architecture, training loops, optimization, checkpoints

### 📊 Results Analyst Agent
- **Role**: Analyze model performance and generate insights
- **Tools**: metrics libraries, statistical analysis
- **Focus**: Accuracy, precision, recall, confusion matrices, reports

### 🎨 Visualization Agent
- **Role**: Create charts, graphs, and visual representations
- **Tools**: matplotlib, plotly, seaborn, altair
- **Focus**: Training curves, performance dashboards, publication-ready plots

### 📝 Publisher Agent
- **Role**: Generate documentation and publish to GitHub Pages
- **Tools**: mkdocs, sphinx, GitHub Actions
- **Focus**: API docs, tutorials, result summaries, deployment

## Code Style Guidelines

- Follow PEP 8 style guidelines
- Use type hints for all function signatures
- Maximum line length: 100 characters (configured in ruff and black)
- Use docstrings for all public functions, classes, and modules
- Prefer explicit over implicit code

## Project Structure

```
src/mcp_b/
├── __init__.py      # Package exports
├── __main__.py      # CLI entry point
├── protocol.py      # MCP-B Protocol (INQC commands)
├── amum.py          # AMUM Alignment workflow
├── qci.py           # QCI Coherence states
├── ethic.py         # ETHIC Principles enforcement
├── bridge.py        # Bridge functionality
├── workflow.py      # Workflow management
└── utils.py         # Utility functions
```

## Key Concepts

### INQC Commands
- **I** (INIT): Initialize connection
- **N** (NODE): Node registration/discovery
- **Q** (QUERY): Request data/state
- **C** (CONNECT): Establish persistent link

### Binary State Flags (16-bit)
Used for connection state tracking with flags for CONNECTED, AUTHENTICATED, ENCRYPTED, etc.

## Testing

- Tests are in `test_utils.py` and should use pytest
- Run tests with: `pytest -v`
- Follow existing test patterns using assertions

## Dependencies

Core dependencies:
- `duckdb>=1.0.0` - Analytics/SQL database
- `surrealdb>=0.3.0` - Graph/Relations database
- `pyyaml>=6.0` - YAML parsing

Dev dependencies:
- `pytest>=7.0` - Testing framework
- `black` - Code formatter
- `ruff` - Linter

## Best Practices

1. Use caching decorators from `utils.py` for performance-critical functions
2. Follow the 4-layer protocol encoding for agent communication
3. Ensure ethical compliance using the ETHIC module
4. Maintain coherence states using QCI for multi-agent systems
5. Use AMUM 3→6→9 alignment for human-AI decision workflows
6. **Always use #serena for code analysis tasks**
7. **Always use #context7 for documentation lookups**
8. Follow the specialized agent roles for ML pipeline tasks

## Workflow Commands

```bash
# Development
pip install -e ".[dev]"      # Install with dev dependencies
pytest -v                     # Run tests
ruff check src/              # Lint code
black src/                   # Format code

# CLI Usage
mcp-b demo                   # Run demo
mcp-b start "task"           # Start workflow
mcp-b status                 # Check status
```
