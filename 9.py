import json

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def calculate_percentage(value, total):
    return (value / total) * 100 if total != 0 else 0

def display_company_info(company_info):
    print("Tên công ty:", company_info["company_name"])
    print("Địa chỉ:", company_info["company_address"])
    print("Tổng số nhân viên:", company_info["total_employees"])
    print("\n-----Thống kê nhân viên theo đơn vị------")

def display_department_stats(departments, total_employees):
    for i, department in enumerate(departments, start=1):
        department_name = department["department_name"]
        num_employees = department["num_employees"]
        percentage = calculate_percentage(num_employees, total_employees)

        print(f"{i}./Tên đơn vị: {department_name}.")
        print(f"- Số nhân viên: {num_employees}.")
        print(f"- Tỷ lệ: {percentage:.2f}%.\n")

if __name__ == "__main__":
    # Đọc dữ liệu từ tệp JSON
    json_data = read_json("9.json")

    # Hiển thị thông tin công ty
    display_company_info(json_data["company_info"])

    # Hiển thị thống kê nhân viên theo đơn vị
    display_department_stats(json_data["departments"], json_data["company_info"]["total_employees"])
