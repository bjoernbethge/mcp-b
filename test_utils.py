#!/usr/bin/env python3
"""
Tests for MCP-B utility functions.

Verifies caching decorators and performance utilities work correctly.
"""

import time
from mcp_b.utils import (
    timed_cache,
    memoize_method,
    batch_operation,
    lazy_property,
    cache_small,
)


def test_timed_cache():
    """Test time-based caching decorator."""
    print("\n[TEST] timed_cache decorator")
    
    call_count = 0
    
    @timed_cache(maxsize=10, ttl_seconds=1)
    def expensive_func(x):
        nonlocal call_count
        call_count += 1
        return x * 2
    
    # First call - should compute
    result1 = expensive_func(5)
    assert result1 == 10
    assert call_count == 1
    
    # Second call - should use cache
    result2 = expensive_func(5)
    assert result2 == 10
    assert call_count == 1  # Not incremented
    
    # Wait for TTL to expire
    time.sleep(1.1)
    
    # Third call - should recompute after TTL
    result3 = expensive_func(5)
    assert result3 == 10
    assert call_count == 2  # Incremented
    
    # Cache info
    info = expensive_func.cache_info()
    assert info['maxsize'] == 10
    assert info['ttl_seconds'] == 1
    
    print("  ✓ Time-based caching works correctly")


def test_memoize_method():
    """Test method memoization decorator."""
    print("\n[TEST] memoize_method decorator")
    
    class Calculator:
        def __init__(self):
            self.compute_count = 0
        
        @memoize_method
        def expensive_calc(self, x, y):
            self.compute_count += 1
            return x * y
    
    calc = Calculator()
    
    # First call - should compute
    result1 = calc.expensive_calc(3, 4)
    assert result1 == 12
    assert calc.compute_count == 1
    
    # Second call with same args - should use cache
    result2 = calc.expensive_calc(3, 4)
    assert result2 == 12
    assert calc.compute_count == 1  # Not incremented
    
    # Different args - should compute
    result3 = calc.expensive_calc(5, 6)
    assert result3 == 30
    assert calc.compute_count == 2
    
    # Test with different instance
    calc2 = Calculator()
    result4 = calc2.expensive_calc(3, 4)
    assert result4 == 12
    assert calc2.compute_count == 1  # Separate cache per instance
    
    print("  ✓ Method memoization works correctly")


def test_batch_operation():
    """Test batch operation decorator."""
    print("\n[TEST] batch_operation decorator")
    
    process_count = 0
    
    @batch_operation(batch_size=3)
    def process_items(items):
        nonlocal process_count
        process_count += 1
        return [x * 2 for x in items]
    
    # Small batch - processed once
    result1 = process_items([1, 2])
    assert result1 == [2, 4]
    assert process_count == 1
    
    # Reset counter
    process_count = 0
    
    # Large batch - should be split
    result2 = process_items([1, 2, 3, 4, 5, 6, 7])
    assert result2 == [2, 4, 6, 8, 10, 12, 14]
    assert process_count == 3  # 7 items / 3 per batch = 3 batches
    
    print("  ✓ Batch operations work correctly")


def test_lazy_property():
    """Test lazy property decorator."""
    print("\n[TEST] lazy_property decorator")
    
    class ExpensiveClass:
        def __init__(self):
            self.compute_count = 0
        
        @lazy_property
        def expensive_property(self):
            self.compute_count += 1
            time.sleep(0.01)  # Simulate expensive computation
            return "computed value"
    
    obj = ExpensiveClass()
    
    # First access - should compute
    value1 = obj.expensive_property
    assert value1 == "computed value"
    assert obj.compute_count == 1
    
    # Second access - should use cached value
    value2 = obj.expensive_property
    assert value2 == "computed value"
    assert obj.compute_count == 1  # Not incremented
    
    # Test with different instance
    obj2 = ExpensiveClass()
    value3 = obj2.expensive_property
    assert value3 == "computed value"
    assert obj2.compute_count == 1  # Separate computation per instance
    
    print("  ✓ Lazy properties work correctly")


def test_cache_small():
    """Test pre-configured small cache."""
    print("\n[TEST] cache_small utility")
    
    call_count = 0
    
    @cache_small
    def cached_func(x):
        nonlocal call_count
        call_count += 1
        return x ** 2
    
    # First call - compute
    result1 = cached_func(5)
    assert result1 == 25
    assert call_count == 1
    
    # Second call - use cache
    result2 = cached_func(5)
    assert result2 == 25
    assert call_count == 1
    
    # Cache info
    info = cached_func.cache_info()
    assert info.maxsize == 32  # cache_small maxsize
    assert info.hits == 1
    assert info.misses == 1
    
    print("  ✓ Pre-configured cache works correctly")


def test_performance_improvement():
    """Verify caching actually improves performance."""
    print("\n[TEST] Performance improvement verification")
    
    # Without cache
    def slow_func(x):
        time.sleep(0.001)
        return x * 2
    
    start = time.perf_counter()
    for _ in range(100):
        slow_func(42)
    no_cache_time = time.perf_counter() - start
    
    # With cache
    @cache_small
    def fast_func(x):
        time.sleep(0.001)
        return x * 2
    
    start = time.perf_counter()
    for _ in range(100):
        fast_func(42)
    cache_time = time.perf_counter() - start
    
    # Cached version should be much faster
    speedup = no_cache_time / cache_time
    print(f"  Speedup: {speedup:.1f}x faster with caching")
    assert speedup > 10, f"Expected >10x speedup, got {speedup:.1f}x"
    
    print("  ✓ Caching provides significant performance improvement")


def main():
    """Run all tests."""
    print("\n" + "="*60)
    print("MCP-B UTILS TEST SUITE")
    print("="*60)
    
    test_timed_cache()
    test_memoize_method()
    test_batch_operation()
    test_lazy_property()
    test_cache_small()
    test_performance_improvement()
    
    print("\n" + "="*60)
    print("ALL TESTS PASSED ✓")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
