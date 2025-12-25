pairs = {"{": "}", "[": "]", "(": ")"}

# Accessing keys that exist
print(pairs["}"])   # Output: }
print(pairs["["])   # Output: ]
print(pairs["("])   # Output: )

# Accessing a key that doesn't exist
try:
    print(pairs["}"])  # This will raise a KeyError
except KeyError:
    print("KeyError! '}' is not a key in the dictionary")