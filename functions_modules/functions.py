# ============================================================
# Topic   : Functions
# Level   : Basic -> Intermediate
# ------------------------------------------------------------
# DEFINITION:
#   A function is a reusable block of code that runs only
#   when it is called. You define it with the keyword def.
#
#   Parameter -> the variable name in the function definition.
#   Argument  -> the actual value you pass when calling it.
#   return    -> sends a value back to the caller.
# ============================================================

# --- 1. Simple function (no parameters, no return) ---
def say_hello():
    print("Hello!")

say_hello()          # calling the function

# --- 2. Function with parameters and return ---
def add(a, b):
    """Return the sum of a and b."""     # docstring = function description
    return a + b

result = add(5, 3)
print("Sum:", result)

# --- 3. Default parameter values ---
def greet(name, msg="Hello"):
    return f"{msg}, {name}!"

print(greet("Yash"))            # uses default
print(greet("Yash", "Hi"))      # overrides default

# --- 4. Keyword arguments (order doesn't matter) ---
print(greet(msg="Good morning", name="Anna"))

# --- 5. Returning multiple values (returns a tuple) ---
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 9, 1, 7])
print("Min:", low, "Max:", high)

# --- 6. A function without return gives None ---
def no_return():
    x = 5

print(no_return())     # None

# --- 7. return stops the function immediately ---
def check_age(age):
    if age < 0:
        return "Invalid age"
    return "Adult" if age >= 18 else "Minor"

print(check_age(-1), check_age(20))

# --- 8. Functions calling other functions ---
def square(n):
    return n * n

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(3, 4))    # 25

# --- 9. Accessing the docstring ---
print(add.__doc__)

# KEY POINTS TO REMEMBER
# - Define once, use many times (DRY: Don't Repeat Yourself).
# - print() shows a value; return gives it back for later use.
# - Default parameters must come AFTER normal parameters.