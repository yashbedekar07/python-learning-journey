# ============================================================
# Topic   : lambda, map, filter, reduce
# Level   : Intermediate
# ------------------------------------------------------------
# DEFINITION:
#   lambda -> a small, anonymous, one-line function.
#             Syntax: lambda arguments: expression
#   map()    -> applies a function to EVERY item of a list.
#   filter() -> keeps only items where the function returns True.
#   reduce() -> combines all items into ONE value (from functools).
# ============================================================

from functools import reduce

# --- 1. lambda vs normal function ---
def square(x):
    return x * x

square_lambda = lambda x: x * x
print(square(5), square_lambda(5))     # 25 25

add = lambda a, b: a + b
print(add(2, 3))                       # 5

nums = [1, 2, 3, 4, 5, 6]

# --- 2. map(): transform every item ---
doubled = list(map(lambda x: x * 2, nums))
print("map    :", doubled)             # [2, 4, 6, 8, 10, 12]

# --- 3. filter(): keep some items ---
evens = list(filter(lambda x: x % 2 == 0, nums))
print("filter :", evens)               # [2, 4, 6]

# --- 4. reduce(): combine into one value ---
product = reduce(lambda a, b: a * b, nums)
print("reduce :", product)             # 720 (1*2*3*4*5*6)

# --- 5. lambda as a sort key (MOST common real use) ---
students = [("Yash", 85), ("Anna", 92), ("Leon", 78)]
by_marks = sorted(students, key=lambda s: s[1], reverse=True)
print("Sorted by marks:", by_marks)

words = ["banana", "kiwi", "apple"]
print(sorted(words, key=len))          # sort by length

# KEY POINTS TO REMEMBER
# - lambda is for SHORT functions. Use def for anything bigger.
# - map/filter return iterators -> wrap with list() to see them.
# - List comprehensions often replace map/filter (see 03_intermediate).