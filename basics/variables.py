# ============================================================
# Topic   : Variables
# Level   : Basic
# ------------------------------------------------------------
# DEFINITION:
#   A variable is a name that stores a value in memory.
#   You create it with the = sign (assignment).
#
# RULES FOR NAMES:
#   - Must start with a letter or underscore (_)
#   - Cannot start with a number
#   - No spaces or special characters (use _ instead)
#   - Case-sensitive: age, Age and AGE are 3 different variables
#   - Cannot be a Python keyword (if, for, class, ...)
# ============================================================

# --- 1. Creating variables ---
name = "Yash"          # text (string)
age = 24               # whole number (int)
height = 5.11          # decimal number (float)
is_student = True      # True / False (bool)

print(name, age, height, is_student)

# --- 2. Variables can change (re-assignment) ---
age = 25
print("New age:", age)

# --- 3. Multiple assignment in one line ---
a, b, c = 1, 2, 3
print(a, b, c)

# --- 4. Same value to many variables ---
x = y = z = 0
print(x, y, z)

# --- 5. Swapping two variables (Python shortcut) ---
a, b = b, a
print("After swap: a =", a, ", b =", b)

# --- 6. Good naming style (snake_case) ---
first_name = "Yash"        # good
total_marks = 450          # good
# 2name = "x"              # ERROR: cannot start with a number
# first name = "x"         # ERROR: no spaces allowed

# --- 7. Constants: Python has none, but we use CAPITAL names by convention ---
PI = 3.14159
MAX_USERS = 100
print(PI, MAX_USERS)

# KEY POINTS TO REMEMBER
# - No need to declare a type. Python decides it (dynamic typing).
# - Use clear names: total_price is better than tp.