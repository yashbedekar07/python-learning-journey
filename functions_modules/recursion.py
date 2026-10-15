# ============================================================
# Topic   : Recursion
# Level   : Intermediate
# ------------------------------------------------------------
# DEFINITION:
#   Recursion is when a function CALLS ITSELF to solve a smaller
#   part of the same problem.
#
#   Every recursive function needs:
#   1. Base case      -> when to STOP
#   2. Recursive case -> call itself with a smaller input
# ============================================================

# --- 1. Factorial: 5! = 5 * 4 * 3 * 2 * 1 ---
def factorial(n):
    if n <= 1:                    # base case
        return 1
    return n * factorial(n - 1)   # recursive case

print("5! =", factorial(5))       # 120

# How it works:
# factorial(5) = 5 * factorial(4)
#              = 5 * 4 * factorial(3)
#              = 5 * 4 * 3 * factorial(2)
#              = 5 * 4 * 3 * 2 * factorial(1)
#              = 5 * 4 * 3 * 2 * 1 = 120

# --- 2. Fibonacci: 0 1 1 2 3 5 8 13 ... ---
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci:", [fibonacci(i) for i in range(10)])

# --- 3. Sum of digits: 1234 -> 1+2+3+4 = 10 ---
def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

print("Sum of digits of 1234:", sum_digits(1234))

# --- 4. Reverse a string ---
def reverse(s):
    if s == "":
        return ""
    return reverse(s[1:]) + s[0]

print(reverse("Python"))

# KEY POINTS TO REMEMBER
# - No base case = infinite calls = RecursionError.
# - Python's default limit is about 1000 nested calls.
# - Loops are often faster; recursion is clearer for trees/nested data.