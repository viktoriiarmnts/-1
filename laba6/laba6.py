def max_arguments(max_args):
    """
    Декоратор, який обмежує максимальну кількість аргументів функції.
    
    Args:
        max_args: Максимально дозволена кількість аргументів
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Підраховуємо загальну кількість аргументів
            total_args = len(args) + len(kwargs)
            
            if total_args > max_args:
                raise ValueError(
                    f"Функція '{func.__name__}' приймає максимум {max_args} аргументів, "
                    f"але передано {total_args}"
                )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator
