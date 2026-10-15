# ============================================================
# Topic   : Tuples and Sets
# Level   : Basic
# ------------------------------------------------------------
# DEFINITION:
#   Tuple -> an ORDERED, IMMUTABLE collection written with ( ).
#            Use it when the data should never change.
#   Set   -> an UNORDERED collection of UNIQUE items written with { }.
#            Use it to remove duplicates or do math-like set operations.
# ============================================================

# ====================== TUPLES ======================

point = (10, 20)
colors = ("red", "green", "blue")

# --- 1. Access like a list ---
print(colors[0], colors[-1], colors[0:2])

# --- 2. Cannot change ---
# colors[0] = "black"     # ERROR: TypeError

# --- 3. Single item tuple needs a comma ---
single = (5,)
not_tuple = (5)
print(type(single), type(not_tuple))   # tuple, int

# --- 4. Unpacking ---
x, y = point
print("x =", x, "y =", y)

# --- 5. Methods (only two) ---
nums = (1, 2, 2, 3)
print(nums.count(2), nums.index(3))

# --- 6. Why use tuples? ---
#   - Faster and safer than lists for fixed data
#   - Can be used as dictionary keys (lists cannot)
location = {(52.39, 13.06): "Potsdam"}
print(location)

# ======================= SETS =======================

a = {1, 2, 3, 3, 3}
print(a)                    # {1, 2, 3}  duplicates removed

# --- 1. Remove duplicates from a list ---
names = ["Anna", "Leon", "Anna", "Yash"]
unique_names = list(set(names))
print(unique_names)

# --- 2. Add / remove ---
a.add(4)
a.discard(10)       # no error if missing
a.remove(1)         # ERROR if missing
print(a)

# --- 3. Set operations ---
x = {1, 2, 3}
y = {3, 4, 5}
print("Union        :", x | y)    # all items
print("Intersection :", x & y)    # common items
print("Difference   :", x - y)    # in x but not in y
print("Symmetric    :", x ^ y)    # in one but not both

# --- 4. Empty set ---
empty_set = set()      # {} creates an empty DICT, not a set!
print(type(empty_set), type({}))

# --- 5. Sets have no index ---
# a[0]                 # ERROR: sets are unordered

# KEY POINTS TO REMEMBER
# - Tuple = list that cannot change.
# - Set = no duplicates, no order, no indexing.
# - Use set() for an empty set, not {}.
