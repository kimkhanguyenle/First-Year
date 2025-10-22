def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)





if __name__ == "__main__":
    print("Fibonacci numbers from 11-20")
    print(f"fibonacci(11) = {fibonacci(11)}")
    print(f"fibonacci(12) = {fibonacci(12)}")
    print(f"fibonacci(13) = {fibonacci(13)}")
    print(f"fibonacci(18) = {fibonacci(18)}")
    print(f"fibonacci(19) = {fibonacci(19)}")
    print(f"fibonacci(20) = {fibonacci(20)}")
    
