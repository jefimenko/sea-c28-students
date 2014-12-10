def function_builder(n):

    l = []
    for s in range(n):
        l.append(lambda a, b=s: a + b)
    return l


c = function_builder(12)
print c[0](1)
print c[11](12)

for b in c:
    print b(3)