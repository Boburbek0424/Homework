from collections import defaultdict

# Create a defaultdict with a default value (e.g., 0 for integers)
my_dict = defaultdict(int)

# Access a missing key, and it will return the default value (0 in this case)
print(my_dict["missing_key"])  # Output: 0
