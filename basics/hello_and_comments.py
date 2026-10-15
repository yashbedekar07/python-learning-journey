# ============================================================
# Topic   : Hello World, print() and Comments
# Level   : Basic
# ------------------------------------------------------------
# DEFINITION:
#   Python is a high-level, interpreted, general-purpose
#   programming language that is easy to read and write.
#
#   print()  -> a built-in function that shows output on screen.
#   Comment  -> text that Python ignores. Used to explain code.
# ============================================================

# --- 1. Your first program ---
print("Hello, World!")

# --- 2. print() can show many values, separated by a space ---
print("Python", "is", "fun")

# --- 3. sep = what goes BETWEEN values, end = what goes at the END ---
print("2026", "10", "15", sep="-")      # 2026-10-15
print("Same line ", end="")             # no new line after this
print("continues here")

# --- 4. Escape characters ---
print("New\nLine")          # \n = new line
print("Tab\tSpace")         # \t = tab
print("He said \"Hi\"")     # \" = quote inside a string

# --- 5. Single-line comment starts with #  (Python skips it) ---

"""
6. Multi-line comment (actually a string that is not used).
   Often used at the top of files or inside functions
   as a 'docstring' to explain what the code does.
"""

# KEY POINTS TO REMEMBER
# - Python runs code from top to bottom, line by line.
# - Python is case-sensitive: print() works, Print() does NOT.