data = {
    "name": "John Doe",
    "age": 30,
    "colors": ["red", "white", "blue"]
}

# Print
print(data["name"])
print(data.get("name"))

# Convert to dict
this_dict = dict(name = "John", age = 36, country = "Norway")
print(this_dict)

# Change value
data["age"] = 50
print(data["age"])

# Add
data["car"] = "Ford"
print(data["car"])

# Remove
data.popitem() # Remove last
print(data)
data.pop("age")
print(data)

# Loop
for x in this_dict:
  print(f"{x}: {this_dict[x]}") # Print key and value


