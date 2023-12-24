import json

# Đối tượng Python mẫu (dictionary)
python_object = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "grades": [95, 88, 92]
}

# Chuyển đối tượng Python thành chuỗi JSON
json_data = json.dumps(python_object, indent=2)

# In ra chuỗi JSON
print("Chuỗi JSON:")
print(json_data)

# In ra tất cả các giá trị
print("\nTất cả các giá trị:")
for key, value in json.loads(json_data).items():
    print(f"{key}: {value}")
