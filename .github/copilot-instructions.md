# GitHub Copilot Instructions for MCP-B

## Project Overview

MCP-B (Master Client Bridge) is a Python package that provides:
- **MCP-B Protocol**: 4-layer encoding for agent-to-agent messaging
- **AMUM**: Progressive 3→6→9 human-AI alignment workflow
- **QCI**: Quantum coherence state tracking
- **ETHIC**: AI ethics principles enforcement

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
