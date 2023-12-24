import json

# Đối tượng từ điển Python mẫu (đã sắp xếp theo khóa)
python_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "grades": [95, 88, 92]
}

# Chuyển đối tượng từ điển Python thành chuỗi JSON với mức thụt lề 4
json_data = json.dumps(python_dict, indent=4)

# In ra chuỗi JSON với mức thụt lề 4
print("Chuỗi JSON:")
print(json_data)
