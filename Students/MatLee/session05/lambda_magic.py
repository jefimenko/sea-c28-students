def function_builder(n):
    return [lambda a, b=s: a + b for s in range(n)]
