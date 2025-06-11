print("hola")


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_value)
    
    return fib_sequence

def main():
    print("Hello, World!")
    print("This is a simple Python script.")
    print("It prints a greeting message to the console.")
    print("Fibonacci sequence for n=10:", fibonacci(10))


if __name__ == "__main__":
    main()
    print("This script is executed directly.")
else:
    print("This script is imported as a module.")
    print("No main function will be executed.")