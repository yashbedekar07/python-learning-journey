# ============================================================
# Topic   : Data Types and Type Conversion
# Level   : Basic
# ------------------------------------------------------------
# DEFINITION:
#   A data type tells Python what KIND of value a variable holds.
#   Type conversion (casting) changes one data type into another.
#
#   int      -> whole number            10
#   float    -> decimal number          3.14
#   str      -> text                    "hello"
#   bool     -> True or False           True
#   list     -> ordered, changeable     [1, 2, 3]
#   tuple    -> ordered, unchangeable   (1, 2, 3)
#   set      -> unordered, unique       {1, 2, 3}
#   dict     -> key: value pairs        {"a": 1}
#   NoneType -> no value                None
# ============================================================

# --- 1. type() tells you the data type ---
print(type(10))           # <class 'int'>
print(type(3.14))         # <class 'float'>
print(type("hello"))      # <class 'str'>
print(type(True))         # <class 'bool'>
print(type([1, 2]))       # <class 'list'>
print(type((1, 2)))       # <class 'tuple'>
print(type({1, 2}))       # <class 'set'>
print(type({"a": 1}))     # <class 'dict'>
print(type(None))         # <class 'NoneType'>

# --- 2. isinstance() checks if a value is a certain type ---
print(isinstance(5, int))      # True

# --- 3. Type conversion ---
print(int("5"))        # str -> int      = 5
print(int(3.99))       # float -> int    = 3 (cuts decimals, no rounding)
print(float(7))        # int -> float    = 7.0
print(str(100))        # int -> str      = "100"
print(list("abc"))     # str -> list     = ['a', 'b', 'c']
print(tuple([1, 2]))   # list -> tuple   = (1, 2)
print(set([1, 1, 2]))  # list -> set     = {1, 2}  (duplicates removed)

# --- 4. bool() conversion: "empty" things are False ---
print(bool(0), bool(""), bool([]), bool(None))   # all False
print(bool(1), bool("hi"), bool([0]))            # all True

# --- 5. Common error ---
# int("hello")   -> ValueError: text that is not a number cannot become int

# --- 6. Why conversion matters ---
print("5" + "5")            # "55"  (string joining)
print(int("5") + int("5"))  # 10    (math)

# KEY POINTS TO REMEMBER
# - input() ALWAYS returns a string -> convert it before doing math.
# - 0, "", [], {}, None are 'falsy'. Everything else is 'truthy'.