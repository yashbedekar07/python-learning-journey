# ============================================================
# Topic   : Dictionaries
# Level   : Basic
# ------------------------------------------------------------
# DEFINITION:
#   A dictionary stores data as KEY: VALUE pairs inside { }.
#   Keys must be unique and immutable (str, int, tuple).
#   Values can be anything. Dictionaries keep insertion order.
# ============================================================

student = {
    "name": "Yash",
    "age": 24,
    "skills": ["Python", "SQL"]
}

# --- 1. Accessing values ---
print(student["name"])                    # Yash
print(student.get("city"))                # None (no error)
print(student.get("city", "Unknown"))     # default value
# print(student["city"])                  # ERROR: KeyError

# --- 2. Add and update ---
student["city"] = "Potsdam"   # add new key
student["age"] = 25           # update existing key
student.update({"course": "MSc Data Science"})
print(student)

# --- 3. Remove ---
removed = student.pop("course")   # remove and return value
del student["city"]               # delete key
print("Removed:", removed)

# --- 4. Keys, values, items ---
print(student.keys())
print(student.values())
print(student.items())

# --- 5. Looping ---
for key in student:
    print(key)

for key, value in student.items():
    print(f"{key} -> {value}")

# --- 6. Check if a key exists ---
print("name" in student)     # True

# --- 7. Nested dictionary ---
class_data = {
    "Yash": {"math": 85, "python": 92},
    "Anna": {"math": 78, "python": 88}
}
print(class_data["Anna"]["python"])    # 88

# --- 8. Counting with a dictionary (very common task) ---
text = "banana"
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1
print(counts)     # {'b': 1, 'a': 3, 'n': 2}

# KEY POINTS TO REMEMBER
# - Use .get() to avoid KeyError.
# - .items() gives key and value together in a loop.
# - Dictionaries are the base of JSON and Pandas DataFrames.