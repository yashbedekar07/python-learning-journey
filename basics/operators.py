# ============================================================
# Topic   : Operators
# Level   : Basic
# ------------------------------------------------------------
# DEFINITION:
#   Operators are symbols that perform operations on values.
#
#   Arithmetic : +  -  *  /  //  %  **
#   Comparison : ==  !=  >  <  >=  <=      -> result is True/False
#   Logical    : and  or  not
#   Assignment : =  +=  -=  *=  /=
#   Membership : in  not in
#   Identity   : is  is not
# ============================================================

a, b = 10, 3

# --- 1. Arithmetic operators ---
print("Add       :", a + b)    # 13
print("Subtract  :", a - b)    # 7
print("Multiply  :", a * b)    # 30
print("Divide    :", a / b)    # 3.333... (always float)
print("Floor div :", a // b)   # 3  (drops decimals)
print("Modulus   :", a % b)    # 1  (remainder)
print("Power     :", a ** b)   # 1000 (10 to the power 3)

# --- 2. Comparison operators ---
print(a == b)    # False  (equal?)
print(a != b)    # True   (not equal?)
print(a > b)     # True
print(a <= b)    # False

# --- 3. Logical operators ---
age, has_ticket = 20, True
print(age >= 18 and has_ticket)   # True only if BOTH are True
print(age < 18 or has_ticket)     # True if AT LEAST ONE is True
print(not has_ticket)             # reverses: True -> False

# --- 4. Assignment operators ---
x = 5
x += 2    # same as x = x + 2  -> 7
x *= 3    # same as x = x * 3  -> 21
x -= 1    # same as x = x - 1  -> 20
print("x =", x)

# --- 5. Membership operators ---
print("a" in "apple")            # True
print(5 not in [1, 2, 3])        # True

# --- 6. Identity operators (same object in memory?) ---
value = None
print(value is None)             # True  (use 'is' for None)

# --- 7. Operator precedence (order of operations) ---
#   ()  ->  **  ->  * / // %  ->  + -  ->  comparisons  ->  not -> and -> or
print(2 + 3 * 4)       # 14, not 20
print((2 + 3) * 4)     # 20, brackets first

# KEY POINTS TO REMEMBER
# - = assigns a value, == compares two values.
# - % is very useful: n % 2 == 0 means n is even.