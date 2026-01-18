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

This project uses specialized Copilot agents for different tasks in the ML/AI pipeline. Each agent is defined in `.github/agents/` as a separate `.agent.md` file with YAML frontmatter.

### Available Agents

The following specialized agents are available:

- **🔬 Data Collector Agent** (`data-collector.agent.md`) - Gather and ingest data from various sources
- **🧹 Data Prep Agent** (`data-prep.agent.md`) - Clean, transform, and prepare data for training  
- **🤖 Model Trainer Agent** (`model-trainer.agent.md`) - Design, train, and optimize ML models
- **📊 Results Analyst Agent** (`results-analyst.agent.md`) - Analyze model performance and generate insights
- **🎨 Visualization Agent** (`visualization.agent.md`) - Create charts, graphs, and visual representations
- **📝 Publisher Agent** (`publisher.agent.md`) - Generate documentation and publish to GitHub Pages

### Using Agents

To invoke a specific agent in your workflow:

```
@agent-name your request here
```

For example:
```
@data-collector help me create a data pipeline to fetch user activity from the GitHub API
@visualization create training curves for these model results
```

Each agent has detailed instructions, code patterns, and best practices in their respective `.agent.md` files.

## Code Style Guidelines

- Follow PEP 8 style guidelines
- Use type hints for all function signatures
- Maximum line length: 100 characters (configured in ruff and black)
- Use docstrings for all public functions, classes, and modules
- Prefer explicit over implicit code
- **Always run `black src/` to format code before committing**
- **Always run `ruff check --fix src/` to fix linting issues**
- Remove unused imports and fix f-string issues flagged by ruff

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
- **Always run tests before committing changes**: `pytest -v`
- If tests fail, ensure your changes are compatible with existing tests
- Don't remove or modify tests unless explicitly required by the task

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
8. Use the specialized agents (`.github/agents/*.agent.md`) for ML pipeline tasks
9. Refer to individual agent files for detailed instructions and code patterns

## Workflow Commands

### Development Setup
```bash
# Install package with dev dependencies
pip install -e ".[dev]"

# Or use uv for faster installation
uv pip install -e ".[dev]"
```

### Code Quality (Always Run Before Committing)
```bash
# Format code with black
black src/

# Lint and fix issues with ruff
ruff check --fix src/

# Or just check without fixing
ruff check src/

# Run all tests
pytest -v

# Run specific test
pytest test_utils.py -v
```

### CLI Usage
```bash
mcp-b demo                   # Run demo
mcp-b version                # Show version
mcp-b encode "Hello" -s 5510 -d 7C1     # Encode message
mcp-b decode "5510 7C1 ..."             # Decode message
mcp-b ethic list                        # List ethical principles
mcp-b qci status                        # QCI network status
```

### Before Creating Pull Requests
Always run these commands to ensure code quality:
```bash
black src/ && ruff check --fix src/ && pytest -v
```
