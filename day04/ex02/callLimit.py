from typing import Any, Callable


def callLimit(limit: int):
    """Decorator factory that creates a decorator to limit function calls"""
    def callLimiter(function: Callable):
        count = 0
        def limit_function(*args: Any, **kwds: Any):
            """Wrapper function that checks the call count before executing"""
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return
            count += 1
            return function(*args, **kwds)
        return limit_function
    return callLimiter
