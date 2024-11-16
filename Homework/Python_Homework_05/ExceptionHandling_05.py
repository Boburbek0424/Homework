try:
    with open('permissionless_file.txt', 'r') as file:
        file.read()
except PermissionError as e:
    print(f"PermissionError: {e}")
