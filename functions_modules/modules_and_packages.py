# ============================================================
# Topic   : Modules and Packages
# Level   : Intermediate
# ------------------------------------------------------------
# DEFINITION:
#   Module  -> a .py file containing functions, classes, variables.
#   Package -> a folder of modules (usually with __init__.py).
#   Library -> a collection of packages (e.g. NumPy, Pandas).
#   import  -> loads a module so you can use its code.
#   pip     -> tool to install external libraries:
#              pip install pandas
# ============================================================

# --- 1. Import the whole module ---
import math
print(math.sqrt(16))        # 4.0
print(math.pi)              # 3.14159...
print(math.ceil(4.2), math.floor(4.8))   # 5 4

# --- 2. Import specific items ---
from random import randint, choice
print(randint(1, 10))                    # random number 1-10
print(choice(["red", "green", "blue"]))  # random item

# --- 3. Import with a short name (alias) ---
import datetime as dt
print(dt.date.today())
#  Data science standard aliases:
#  import numpy as np
#  import pandas as pd
#  import matplotlib.pyplot as plt

# --- 4. Useful built-in modules ---
import os
import sys
print("Current folder:", os.getcwd())
print("Python version:", sys.version.split()[0])

# --- 5. See what a module contains ---
print(dir(math)[:10])

# --- 6. Importing your OWN module ---
#   If you have a file called my_utils.py in the same folder:
#       def greet(name):
#           return f"Hi {name}"
#   Then in another file:
#       import my_utils
#       print(my_utils.greet("Yash"))

# --- 7. if __name__ == "__main__" ---
#   Code inside this block runs ONLY when you run this file directly,
#   NOT when another file imports it.
def main():
    print("Running this file directly")

if __name__ == "__main__":
    main()

# KEY POINTS TO REMEMBER
# - Avoid 'from module import *' (it hides where names come from).
# - Don't name your file the same as a module (e.g. math.py, random.py),
#   or Python will import YOUR file instead.