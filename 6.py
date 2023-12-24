import json
file_json = input()
# Đọc từ tệp JSON
with open(file_json, 'r') as file:
    python_object = json.load(file)

# In đối tượng Python
print("Đối tượng Python:", python_object)
