d = {}  # Initialize an empty dictionary

user_input = [1, 2, 3, 4, 4, 4, 5, 5]  # Input list

# Count occurrences of each element in user_input
for el in user_input:
    d.setdefault(el, 0)  # Initialize dictionary key if it doesn't exist
    d[el] += 1  # Increment count for the element

# Print key-value pairs from the dictionary
for key, value in d.items():
    print(key, value)

# Identify unique and duplicate occurrences
unique = [v for v in d.values() if v == 1]  # Counts of elements appearing exactly once
dup = [v for v in d.values() if v > 1]  # Counts of elements appearing more than once
print(unique)
print(dup)


