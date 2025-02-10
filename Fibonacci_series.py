def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):  
        yield a
        a, b = b, a + b

n = int(input("Enter the number of Fibonacci series you wanna generate: "))  
fib_list = list(fibonacci_series(n))

i = 0
for level in range(1, len(fib_list) + 1):
    if i + level > len(fib_list):
        break
    print(*fib_list[i:i + level])
    i += level
