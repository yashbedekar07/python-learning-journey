# ============================================================
# Topic   : Variable Scope (LEGB rule)
# Level   : Intermediate
# ------------------------------------------------------------
# DEFINITION:
#   Scope is the area of the program where a variable can be used.
#
#   Python searches for a name in this order (LEGB):
#   L - Local     : inside the current function
#   E - Enclosing : inside an outer function (for nested functions)
#   G - Global    : at the top level of the file
#   B - Built-in  : Python's own names (print, len, ...)
# ============================================================

x = "global x"                 # Global scope

def outer():
    x = "enclosing x"          # Enclosing scope

    def inner():
        x = "local x"          # Local scope
        print("inner sees:", x)

    inner()
    print("outer sees:", x)

outer()
print("file sees:", x)

# --- 1. Local variables don't exist outside the function ---
def make_local():
    secret = 42
    return secret

make_local()
# print(secret)                # ERROR: NameError

# --- 2. Changing a global variable inside a function ---
counter = 0

def increase():
    global counter             # tell Python to use the global one
    counter += 1

increase()
increase()
print("counter =", counter)    # 2

# --- 3. nonlocal: change an enclosing variable ---
def outer_counter():
    count = 0
    def add_one():
        nonlocal count
        count += 1
    add_one()
    add_one()
    return count

print("nonlocal count =", outer_counter())   # 2

# KEY POINTS TO REMEMBER
# - Avoid 'global' where possible; pass values as parameters
#   and return results instead. It keeps code clean.