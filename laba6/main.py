from decorator import limit_args

@limit_args(2)  
def add(a, b):
    return a + b

@limit_args(3)   
def info(name, age, city):
    return f"{name}, {age}, {city}"
