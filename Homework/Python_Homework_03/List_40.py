List = [12, 423, 12, 32, 32]
New_List = list(dict.fromkeys(List)) # dict.fromkeys for conserving order
print("Unique values' list:", New_List)
