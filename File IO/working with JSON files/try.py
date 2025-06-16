import json

# Python dictionary
data = {
    "name": "Alice",
    "age": 25,
    "is_active": True,
    "skills": ["Python", "Data Analysis"]
}

# Convert Python dict to JSON string (serialization)
json_string = json.dumps(data, indent=4)  # indent for pretty printing
print(json_string,"\n")
print(type(json_string))

# Convert JSON string back to Python dict (deserialization)
python_dict = json.loads(json_string)
print(python_dict["name"],"\n")  # Output: Alice
print(python_dict,"\n")


# Writing to a JSON file
with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)

# Reading from a JSON file
with open('output.json', 'r') as f:
    loaded_data = json.load(f)
    print(loaded_data)
    print(type(loaded_data))
