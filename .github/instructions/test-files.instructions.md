---
applyTo: "**/test_*.py"
---

# Test File Instructions

When writing or modifying test files in this repository, follow these guidelines:

## Test Structure

### File Naming
- Test files must start with `test_`: `test_utils.py`, `test_protocol.py`
- Test functions must start with `test_`: `test_encode_message()`

### Test Organization
```python
import pytest
from mcp_b.module import function_to_test

def test_function_with_valid_input():
    """Test that function works correctly with valid input."""
    result = function_to_test("valid")
    assert result == expected_value

def test_function_with_invalid_input():
    """Test that function raises error with invalid input."""
    with pytest.raises(ValueError):
        function_to_test("invalid")
```

## Test Patterns

### Use Descriptive Names
Test names should clearly describe what is being tested:

```python
# Good
def test_encode_mcb_creates_valid_message_format():
    """Test that encode_mcb returns message in correct format."""
    pass

# Bad
def test_encode():
    """Test encode."""
    pass
```

### Use Fixtures for Setup
```python
@pytest.fixture
def sample_agent():
    """Create a sample MCBAgent for testing."""
    return MCBAgent(agent_id="7C1", name="TestAgent")

def test_agent_creation(sample_agent):
    """Test agent is created correctly."""
    assert sample_agent.agent_id == "7C1"
    assert sample_agent.name == "TestAgent"
```

### Test Edge Cases
Always test:
- Valid inputs (happy path)
- Invalid inputs (error cases)
- Boundary conditions (empty, null, max values)
- Edge cases specific to the function

```python
def test_cache_with_empty_data():
    """Test cache handles empty data correctly."""
    assert cache_function([]) == []

def test_cache_with_large_data():
    """Test cache handles large datasets."""
    large_data = list(range(10000))
    result = cache_function(large_data)
    assert len(result) == 10000
```

### Use Assertions Effectively
```python
# Good - specific assertions
assert result == expected
assert result > 0
assert "key" in result
assert isinstance(result, dict)

# Also good - pytest assertions with messages
assert result == expected, f"Expected {expected}, got {result}"
```

## Running Tests

### Run All Tests
```bash
pytest -v
```

### Run Specific Test File
```bash
pytest test_utils.py -v
```

### Run Specific Test Function
```bash
pytest test_utils.py::test_timed_cache -v
```

### Run Tests with Coverage
```bash
pytest --cov=mcp_b --cov-report=html
```

## Test Performance

When testing performance-critical code:

```python
import time

def test_cache_improves_performance():
    """Test that caching improves performance significantly."""
    # First call (uncached)
    start = time.time()
    result1 = expensive_function()
    time1 = time.time() - start
    
    # Second call (cached)
    start = time.time()
    result2 = expensive_function()
    time2 = time.time() - start
    
    # Cached should be significantly faster
    assert result1 == result2
    assert time2 < time1 * 0.1  # At least 10x faster
```

## Mocking and Patching

When tests need to mock external dependencies:

```python
from unittest.mock import Mock, patch

@patch('mcp_b.protocol.datetime')
def test_timestamp_generation(mock_datetime):
    """Test timestamp generation with mocked datetime."""
    mock_datetime.now.return_value = datetime(2024, 1, 1)
    result = generate_timestamp()
    assert result == "2024-01-01T00:00:00"
```

## What NOT to Do

- ❌ Don't remove or modify existing tests unless explicitly required
- ❌ Don't skip tests with `@pytest.mark.skip` without a good reason
- ❌ Don't test implementation details, test behavior
- ❌ Don't make tests dependent on each other
- ❌ Don't use sleep() for timing - use proper timing measurements

## Test Quality Checklist

Before committing test changes, verify:
- [ ] All tests have descriptive names and docstrings
- [ ] Tests cover both success and failure cases
- [ ] Tests are independent and can run in any order
- [ ] Tests run quickly (< 1 second each when possible)
- [ ] All assertions are specific and clear
- [ ] No commented-out test code
- [ ] All tests pass: `pytest -v`
