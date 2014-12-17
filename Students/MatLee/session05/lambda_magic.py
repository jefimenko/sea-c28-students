def function_builder(n):
    return [lambda a, b=s: a + b for s in range(n)]

if __name__ == "__main__":
    a = function_builder(10)
    for c in range(3):
        print [i(c) for i in a]