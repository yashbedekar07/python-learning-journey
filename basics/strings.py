# ============================================================
# Topic   : Strings
# Level   : Basic
# ------------------------------------------------------------
# DEFINITION:
#   A string is a sequence of characters inside quotes.
#   Strings are IMMUTABLE: you cannot change them in place,
#   every method returns a NEW string.
# ============================================================

s = "Python Programming"

# --- 1. Indexing (positions start at 0) ---
#    P  y  t  h  o  n
#    0  1  2  3  4  5
#   -6 -5 -4 -3 -2 -1
print(s[0])      # P   (first character)
print(s[-1])     # g   (last character)

# --- 2. Slicing: s[start : stop : step]  (stop is NOT included) ---
print(s[0:6])    # Python
print(s[7:])     # Programming   (from 7 to end)
print(s[:6])     # Python        (from start to 6)
print(s[::2])    # every 2nd character
print(s[::-1])   # reversed string

# --- 3. Length ---
print(len(s))    # 18

# --- 4. Common string methods ---
print(s.upper())                 # PYTHON PROGRAMMING
print(s.lower())                 # python programming
print("hello world".title())     # Hello World
print(s.replace("Python", "Java"))
print(s.find("Pro"))             # 7  (index where it starts, -1 if not found)
print(s.count("m"))              # 2
print(s.startswith("Py"))        # True
print(s.endswith("ing"))         # True

# --- 5. Cleaning text ---
messy = "   hello   "
print("[" + messy.strip() + "]")    # removes spaces from both sides

# --- 6. split() and join() ---
csv_line = "apple,banana,mango"
fruits = csv_line.split(",")        # string -> list
print(fruits)                       # ['apple', 'banana', 'mango']
print(" | ".join(fruits))           # list -> string

# --- 7. Checking content ---
print("123".isdigit())      # True
print("abc".isalpha())      # True
print("abc123".isalnum())   # True

# --- 8. Strings are immutable ---
# s[0] = "J"                 # ERROR: TypeError
new_s = "J" + s[1:]          # create a NEW string instead
print(new_s)

# --- 9. Multi-line strings ---
poem = """Line one
Line two"""
print(poem)

# KEY POINTS TO REMEMBER
# - Index starts at 0. Negative index counts from the end.
# - Slicing stop value is NOT included.
# - split() makes a list, join() makes a string.