import json

# Python dictionary
data = {
    "name": "Alice",
    "age": 25,
    "is_active": True,
    "skills": ["Python", "Data Analysis"]
}

json_str=json.dumps(data) #json.dumps() converts python dict to json string(SERIALISATION)
print(json_str)

py_dict=json.loads(json_str) #json.loads() converts json str to py dict(DESERIALISATION)
print(py_dict["name"])

with open("output.json","w") as f:
    json.dump(data,f,indent=4)

with open("output.json","r") as f:
    json_data=json.load(f)
    print(json_data)

