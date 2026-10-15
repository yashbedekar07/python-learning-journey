# ============================================================
# Topic   : Conditional Statements (if / elif / else)
# Level   : Basic
# ------------------------------------------------------------
# DEFINITION:
#   Conditional statements run a block of code ONLY when a
#   condition is True. Python uses INDENTATION (4 spaces)
#   to know which lines belong to which block.
# ============================================================

marks = 75

# --- 1. if / elif / else ---
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

# --- 2. Multiple conditions with and / or ---
age = 20
has_id = True
if age >= 18 and has_id:
    print("Entry allowed")

# --- 3. Nested if ---
if age >= 18:
    if has_id:
        print("Adult with ID")
    else:
        print("Adult without ID")

# --- 4. One-line if (ternary operator) ---
status = "Adult" if age >= 18 else "Minor"
print(status)

# --- 5. Truthy / falsy check ---
cart = []
if not cart:
    print("Cart is empty")

# --- 6. Chained comparison ---
temp = 22
if 18 <= temp <= 25:
    print("Nice weather")

# --- 7. match-case (Python 3.10+), like switch in other languages ---
day = "sat"
match day:
    case "sat" | "sun":
        print("Weekend")
    case "mon":
        print("Start of week")
    case _:                 # _ means 'anything else'
        print("Weekday")

# KEY POINTS TO REMEMBER
# - Only the FIRST True branch runs in an if/elif chain.
# - Don't forget the colon : at the end of if/elif/else.
# - Wrong indentation = IndentationError.