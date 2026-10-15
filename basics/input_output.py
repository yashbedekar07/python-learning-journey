# ============================================================
# Topic   : Input and Output
# Level   : Basic
# ------------------------------------------------------------
# DEFINITION:
#   input()  -> takes data from the user (keyboard).
#               It ALWAYS returns a string.
#   print()  -> shows output on the screen.
#   f-string -> a string with f in front, lets you put
#               variables inside { } directly.
# ============================================================

# --- 1. Taking input ---
name = input("Enter your name: ")

# --- 2. Converting input to a number ---
age = int(input("Enter your age: "))

# --- 3. Three ways to print variables ---
print("Hello", name, "you are", age)                   # comma style
print("Hello " + name + " you are " + str(age))        # + joining (needs str)
print(f"Hello {name}, you are {age}")                  # f-string (BEST)

# --- 4. Math inside an f-string ---
print(f"Next year you will be {age + 1}")

# --- 5. Formatting numbers ---
price = 1234.5678
print(f"Price: {price:.2f}")       # 2 decimal places  -> 1234.57
print(f"Price: {price:,.2f}")      # with comma        -> 1,234.57
print(f"{0.856:.1%}")              # as percent        -> 85.6%
print(f"[{name:>10}]")             # right-align in 10 spaces
print(f"[{name:<10}]")             # left-align in 10 spaces

# KEY POINTS TO REMEMBER
# - Always convert input with int() or float() before doing math.
# - f-strings are the modern, cleanest way to format output.