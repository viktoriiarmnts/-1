def limit_args(max_args):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_args = len(args) + len(kwargs)

            if total_args > max_args:
                return f"❌ Функцію '{func.__name__}' НЕ виконано — забагато аргументів! (отримано {total_args}, дозволено {max_args})"
            
            return func(*args, **kwargs)
        return wrapper
    return decorator
