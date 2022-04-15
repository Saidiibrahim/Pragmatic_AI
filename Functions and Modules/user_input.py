# File level doc string
"""
Create a function that given some input (string)
will output True or False.
True values in strings are like "1", "Y", "Yes"
False values are like "0", "N", "N0"
"""

def str_to_bool(string):
    string = string.lower()
    true_vals = ["1", "y", "yes"]
    false_vals = ["0", "n", "no"]
    if string in true_vals:
        return True
    elif string in false_vals:
        return False
    print(f"Do not know what happened. Value {string}")

#print(str_to_bool())

# End note: A module in Python is a file.
# If we define a function in a module, we
# can import them elsewhere
# This is ideal for good structuring and organisation
# and separation of concerns
# We could have called this file utils or helpers,
# but helpers for what. Try to be explicit whenever possible