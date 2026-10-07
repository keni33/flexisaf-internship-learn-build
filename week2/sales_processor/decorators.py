from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import Any

def measure_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """Measure and print how long a function takes to run."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter()

        result = func(*args, **kwargs)

        end_time = perf_counter()

        elapsed_time = end_time - start_time

        print(
            f"{func.__name__} took "
            f"{elapsed_time:.6f} seconds"
        )

        return result

    return wrapper

