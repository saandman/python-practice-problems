# Write a Python script to sort (ascending and descending) a dictionary by value.

sample_dict = {"a": 6, "b": 8, "c": 4, "d": 10}

# Ascending order
sorted_dict = {dict_key: dict_value for dict_key, dict_value in sorted(sample_dict.items(), key=lambda item: item[1], reverse=False)}

# Descending order
# sorted_dict = {dict_key: dict_value for dict_key, dict_value in sorted(sample_dict.items(), key=lambda item: item[1], reverse=True)}

print(sorted_dict)
