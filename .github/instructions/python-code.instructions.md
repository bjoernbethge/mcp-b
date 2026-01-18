---
applyTo: "**/*.py"
---

# Python Code Instructions

When working with Python files in this repository, follow these specific guidelines:

## Code Quality Requirements

### Before Every Commit
1. **Format with black**: `black src/` or `black <file>`
2. **Lint with ruff**: `ruff check --fix src/` or `ruff check --fix <file>`
3. **Run tests**: `pytest -v` to ensure nothing breaks

### Type Hints
- All function parameters must have type hints
- All return values must have type hints
- For Python 3.11+, prefer built-in generic types: `list`, `dict`, `tuple`
- Use union syntax `X | None` instead of `Optional[X]`
- Import from `typing` only when needed: `Any`, `Callable`, etc.

Example:
```python
from typing import Any

def process_data(data: dict[str, Any], timeout: int | None = None) -> bool:
    """Process data with optional timeout."""
    pass
```

### Docstrings
- All public functions, classes, and modules must have docstrings
- Use triple quotes: `"""`
- Include description, parameters, returns, and raises sections when appropriate

Example:
```python
from typing import Any

def encode_message(source: str, dest: str, payload: dict[str, Any]) -> str:
    """
    Encode a message using MCP-B protocol.
    
    Args:
        source: Source agent ID (hex format)
        dest: Destination agent ID (hex format)
        payload: Message payload as dictionary
        
    Returns:
        Encoded message string
        
    Raises:
        ValueError: If source or dest are invalid
    """
    pass
```

### Imports
- Remove unused imports (ruff will flag these)
- Group imports: standard library, third-party, local
- Use absolute imports for project modules: `from mcp_b.protocol import MCBAgent`

### F-strings
- Use f-strings for string formatting
- Remove unnecessary `f` prefix when there are no placeholders
- Example: Use `print("Hello")` not `print(f"Hello")`

## Common Patterns

### Error Handling
```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    raise
```

### Dataclasses for Data Structures
```python
from dataclasses import dataclass

@dataclass
class MCBAgent:
    agent_id: str
    name: str
    capabilities: list[str] | None = None
```

### Performance Decorators
Use caching decorators from `utils.py` when appropriate:
```python
from mcp_b.utils import timed_cache, memoize_method

@timed_cache(ttl=60)
def expensive_computation(x: int) -> int:
    return x * x
```

## Project-Specific Conventions

### Binary Flags
When working with binary state flags, use clear bit operations:
```python
# Good
flags = 0b1011101010111111
is_connected = bool(flags & (1 << 0))

# Bad
is_connected = flags & 1
```

### INQC Commands
Always validate INQC command types:
```python
from mcp_b.protocol import INQCCommand

# Use enum values
command = INQCCommand.QUERY

# Not magic strings
# command = "Q"  # Bad
```

## Testing
- Write unit tests for new functionality
- Use pytest fixtures for setup/teardown
- Follow naming convention: `test_<function_name>`
- Use descriptive test names that explain what is being tested

```python
def test_encode_mcb_with_valid_inputs():
    """Test that encode_mcb correctly encodes valid inputs."""
    result = encode_mcb("5510", "7C1", 0xBEBF, "Q", {"ping": True})
    assert "5510" in result
    assert "7C1" in result
```
