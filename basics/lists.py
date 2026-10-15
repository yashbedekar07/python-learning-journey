# ============================================================
# Topic   : Lists
# Level   : Basic
# ------------------------------------------------------------
# DEFINITION:
#   A list is an ORDERED, MUTABLE (changeable) collection
#   written with square brackets [ ]. It allows duplicates
#   and can hold different data types.
# ============================================================

fruits = ["apple", "banana", "mango"]
mixed = [1, "two", 3.0, True]       # different types allowed
print(fruits, mixed)

# --- 1. Accessing items (same indexing/slicing as strings) ---
print(fruits[0])       # apple
print(fruits[-1])      # mango
print(fruits[0:2])     # ['apple', 'banana']

# --- 2. Changing an item (lists are mutable) ---
fruits[1] = "kiwi"
print(fruits)          # ['apple', 'kiwi', 'mango']

# --- 3. Adding items ---
fruits.append("grape")          # add at the END
fruits.insert(1, "orange")      # add at a POSITION
fruits.extend(["pear", "plum"]) # add MANY items
print(fruits)

# --- 4. Removing items ---
fruits.remove("pear")    # remove by VALUE (first match)
last = fruits.pop()      # remove LAST item and return it
first = fruits.pop(0)    # remove by INDEX
print("Removed:", last, first)
print(fruits)
# del fruits[0]          # delete by index
# fruits.clear()         # empty the list

# --- 5. Searching ---
print("mango" in fruits)       # True
print(fruits.index("mango"))   # position of mango
print([1, 2, 2, 3].count(2))   # 2

# --- 6. Sorting ---
nums = [5, 2, 9, 1]
nums.sort()                    # changes the list itself
print(nums)                    # [1, 2, 5, 9]
nums.sort(reverse=True)
print(nums)                    # [9, 5, 2, 1]
print(sorted([3, 1, 2]))       # returns a NEW sorted list
nums.reverse()
print(nums)

# --- 7. Useful built-in functions ---
scores = [70, 85, 90, 60]
print(len(scores), sum(scores), min(scores), max(scores))
print("Average:", sum(scores) / len(scores))

# --- 8. Copying a list (IMPORTANT) ---
a = [1, 2, 3]
b = a            # NOT a copy, both names point to the SAME list
c = a.copy()     # a real copy
a.append(4)
print("b:", b)   # [1, 2, 3, 4]  -> changed too!
print("c:", c)   # [1, 2, 3]     -> safe

# --- 9. Nested list (list inside a list) ---
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])   # 3

# --- 10. Looping through a list ---
for fruit in fruits:
    print("Fruit:", fruit)

# KEY POINTS TO REMEMBER
# - append() adds one item, extend() adds many.
# - sort() changes the list, sorted() returns a new one.
# - b = a does NOT copy. Use a.copy().