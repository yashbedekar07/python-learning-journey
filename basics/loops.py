# ============================================================
# Topic   : Loops (for, while, break, continue, pass)
# Level   : Basic
# ------------------------------------------------------------
# DEFINITION:
#   A loop repeats a block of code.
#   for loop   -> repeats over a sequence (list, string, range).
#   while loop -> repeats as long as a condition is True.
#   break      -> stops the loop completely.
#   continue   -> skips the rest of this round, goes to the next.
#   pass       -> does nothing (placeholder).
# ============================================================

# --- 1. range(start, stop, step)  (stop is NOT included) ---
for i in range(5):           # 0 1 2 3 4
    print(i, end=" ")
print()

for i in range(1, 11, 2):    # 1 3 5 7 9
    print(i, end=" ")
print()

for i in range(5, 0, -1):    # 5 4 3 2 1 (counting down)
    print(i, end=" ")
print()

# --- 2. Loop through a list and a string ---
for fruit in ["apple", "mango"]:
    print(fruit)

for ch in "Hi!":
    print(ch)

# --- 3. while loop ---
count = 1
while count <= 3:
    print("Count:", count)
    count += 1               # IMPORTANT: otherwise infinite loop

# --- 4. break ---
for n in range(10):
    if n == 5:
        break                # stop at 5
    print(n, end=" ")
print()

# --- 5. continue ---
for n in range(6):
    if n % 2 == 0:
        continue             # skip even numbers
    print(n, end=" ")        # 1 3 5
print()

# --- 6. pass ---
for n in range(3):
    pass                     # TODO: write code later

# --- 7. else with loops (runs if loop did NOT break) ---
for n in [1, 3, 5]:
    if n % 2 == 0:
        print("Found even")
        break
else:
    print("No even number found")

# --- 8. Nested loops (multiplication table) ---
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="\t")
    print()

# --- 9. Common patterns ---
total = 0
for n in range(1, 101):
    total += n
print("Sum of 1 to 100:", total)       # 5050

for i in range(1, 5):                  # star pattern
    print("*" * i)

# KEY POINTS TO REMEMBER
# - Use for when you know how many times; while when you don't.
# - Always update the while condition or it runs forever.