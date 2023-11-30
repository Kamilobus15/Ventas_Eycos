import json

# Read JSON data from file
with open('anual2023.json', 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

# Count the number of key-value pairs
num_objects = len(json_data)

print(f'The JSON document has {num_objects} key-value pairs.')