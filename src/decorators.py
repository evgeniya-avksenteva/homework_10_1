from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Callable:
    """Декоратор логирует начало и конец функции,
    а также ее результаты или возникшие ошибки"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} called with args: {args}, kwargs:{kwargs}. Result: {result}"
                with open(filename, "a") as f:
                    f.write(log_message + "\n")
                print(log_message)
            except Exception as e:
                error_message = f"{func.__name__} error: {e}. Inputs:{args}, {kwargs}"
                with open(filename, "a") as f:
                    f.write(error_message + "\n")
                print(error_message)

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: str, y: str) -> str:
    return x + y


my_function(1, 2)
