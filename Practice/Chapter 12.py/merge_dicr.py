dict1 = { "a": 1, "b": 2}
dict2 = { "b": 3, "c": 4}

# Merge dictionaries
merged_dict =  dict1 | dict2
print(merged_dict)  

# Output: {'a': 1, 'b': 3, 'c': 4}
#"b" : 2 is overwritten by "b": 3 from dict2 because dict2 is merged into dict1. OOP concept is used here. 
# The merged dictionary contains all unique keys from both dictionaries, with values from dict2 taking precedence in case of key conflicts.