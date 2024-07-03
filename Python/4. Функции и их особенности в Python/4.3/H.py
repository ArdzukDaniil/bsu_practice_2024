def fibonacci(count):
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b
