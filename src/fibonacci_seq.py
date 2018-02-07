"""

Write a function fib() that takes an integer n and returns the nth Fibonacci number.

Let's say our Fibonacci series is 0-indexed and starts with 0. 

"""

def fib(n):
    if n in [0, 1]:
        return n
    
    memo = {}

    if memo.contains(n):
        return memo[n]

    

    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    fib(0)  # 0
    fib(1)  # 1
    fib(2)  # 1
    fib(3)  # 2
    fib(4)  # 3
    fib(12) # 12
