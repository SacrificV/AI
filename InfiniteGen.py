def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

fib = fibonacci()
for _ in range(50):
    print(next(fib))