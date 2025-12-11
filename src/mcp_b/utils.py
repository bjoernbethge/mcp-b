"""
Utility functions for MCP-B.

Includes performance optimization utilities like caching decorators.
"""

from functools import wraps, lru_cache
from typing import Callable, Any
import time


def timed_cache(maxsize: int = 128, ttl_seconds: float = 300):
    """
    Decorator that caches function results with a time-to-live.
    
    Args:
        maxsize: Maximum cache size
        ttl_seconds: Time to live for cached results in seconds
    
    Example:
        @timed_cache(maxsize=100, ttl_seconds=60)
        def expensive_operation(x):
            return x * 2
    """
    def decorator(func: Callable) -> Callable:
        cache = {}
        timestamps = {}
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key from args and kwargs
            key = (args, tuple(sorted(kwargs.items())))
            current_time = time.time()
            
            # Check if cached and not expired
            if key in cache:
                if current_time - timestamps[key] < ttl_seconds:
                    return cache[key]
            
            # Compute result
            result = func(*args, **kwargs)
            
            # Update cache with LRU eviction
            if len(cache) >= maxsize:
                # Remove oldest entry
                oldest_key = min(timestamps, key=timestamps.get)
                del cache[oldest_key]
                del timestamps[oldest_key]
            
            cache[key] = result
            timestamps[key] = current_time
            return result
        
        # Add cache management methods
        wrapper.cache_clear = lambda: (cache.clear(), timestamps.clear())
        wrapper.cache_info = lambda: {
            "size": len(cache),
            "maxsize": maxsize,
            "ttl_seconds": ttl_seconds
        }
        
        return wrapper
    return decorator


def memoize_method(func: Callable) -> Callable:
    """
    Decorator to memoize instance methods (cache per instance).
    
    Example:
        class MyClass:
            @memoize_method
            def expensive_method(self, x):
                return x * 2
    """
    cache_attr = f"_cache_{func.__name__}"
    
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # Get or create cache for this instance
        if not hasattr(self, cache_attr):
            setattr(self, cache_attr, {})
        
        cache = getattr(self, cache_attr)
        key = (args, tuple(sorted(kwargs.items())))
        
        if key not in cache:
            cache[key] = func(self, *args, **kwargs)
        
        return cache[key]
    
    return wrapper


def batch_operation(batch_size: int = 100):
    """
    Decorator to batch operations for better performance.
    
    Args:
        batch_size: Number of items to process in each batch
    
    Example:
        @batch_operation(batch_size=50)
        def process_items(items):
            return [item * 2 for item in items]
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(items):
            if len(items) <= batch_size:
                return func(items)
            
            results = []
            for i in range(0, len(items), batch_size):
                batch = items[i:i + batch_size]
                results.extend(func(batch))
            return results
        
        return wrapper
    return decorator


# Pre-configured LRU caches for common use cases
cache_small = lru_cache(maxsize=32)
cache_medium = lru_cache(maxsize=128)
cache_large = lru_cache(maxsize=512)


def lazy_property(func: Callable) -> property:
    """
    Decorator for lazy-loaded properties that are computed once.
    
    Example:
        class MyClass:
            @lazy_property
            def expensive_property(self):
                return compute_something_expensive()
    """
    attr_name = f"_lazy_{func.__name__}"
    
    @wraps(func)
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, func(self))
        return getattr(self, attr_name)
    
    return property(wrapper)
