# File level doc string
"""
Create a function that given some input (string)
will output True or False.
True values in strings are like "1", "Y", "Yes"
False values are like "0", "N", "N0"


function_input = "1"
true_vals = ["1", "Y", "Yes"]
false_vals = ["0", "N", "No"]
if function_input in true_vals:
    print("True")
elif function_input in false_vals:
    print("False")
"""

def str_to_bool(string):
    true_vals = ["1", "Y", "Yes"]
    false_vals = ["0", "N", "No"]
    if string in true_vals:
        return True
    elif string in false_vals:
        return False

print(str_to_bool())