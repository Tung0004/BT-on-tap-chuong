class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return f"{self.day}/{self.month}/{self.year}"

class Employee:
    def __init__(self, full_name, birth_date, hire_date):
        self.full_name = full_name
        self.birth_date = birth_date
        self.hire_date = hire_date

    def display_employee_info(self):
        print("Họ tên:", self.full_name)
        print("Ngày sinh:", self.birth_date.display())
        print("Ngày vào công ty:", self.hire_date.display())

# Chương trình chính
if __name__ == "__main__":
    employees = []

    while True:
        print("\n1. Thêm nhân viên")
        print("2. Hiển thị thông tin nhân viên")
        print("3. Thoát")
        choice = int(input("Chọn thao tác: "))

        if choice == 1:
            full_name = input("Nhập họ tên nhân viên: ")
            day, month, year = map(int, input("Nhập ngày tháng năm sinh (ngày/tháng/năm): ").split("/"))
            birth_date = Date(day, month, year)
            day, month, year = map(int, input("Nhập ngày tháng năm vào công ty (ngày/tháng/năm): ").split("/"))
            hire_date = Date(day, month, year)

            employee = Employee(full_name, birth_date, hire_date)
            employees.append(employee)
        elif choice == 2:
            if not employees:
                print("Danh sách nhân viên trống.")
            else:
                for idx, employee in enumerate(employees, start=1):
                    print(f"\nNhân viên {idx}:")
                    employee.display_employee_info()
        elif choice == 3:
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
