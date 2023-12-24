class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []
        self.top = -1

    def push(self, item):
        if not self.is_full():
            self.stack.append(item)
            self.top += 1
        else:
            print("Ngăn xếp đã đầy. Không thể thêm phần tử.")

    def pop(self):
        if not self.is_empty():
            popped_item = self.stack.pop()
            self.top -= 1
            return popped_item
        else:
            print("Ngăn xếp đã trống. Không thể lấy phần tử.")

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def count(self):
        return self.top + 1

    def print_stack(self):
        if self.is_empty():
            print("Ngăn xếp rỗng.")
        else:
            print("Nội dung của ngăn xếp:")
            for item in self.stack:
                print(item)

def menu():
    print("\n1. Push (Thêm phần tử)")
    print("2. Pop (Lấy phần tử)")
    print("3. Kiểm tra ngăn xếp rỗng")
    print("4. Kiểm tra ngăn xếp đầy")
    print("5. Số phần tử trên ngăn xếp")
    print("6. In nội dung của ngăn xếp")
    print("7. Thoát")

def main():
    max_size = int(input("Nhập kích thước tối đa của ngăn xếp: "))
    my_stack = Stack(max_size)

    while True:
        menu()
        choice = int(input("Chọn thao tác: "))

        if choice == 1:
            item = float(input("Nhập giá trị phần tử: "))
            my_stack.push(item)
        elif choice == 2:
            popped_item = my_stack.pop()
            if popped_item is not None:
                print("Phần tử lấy ra:", popped_item)
        elif choice == 3:
            print("Ngăn xếp rỗng." if my_stack.is_empty() else "Ngăn xếp không rỗng.")
        elif choice == 4:
            print("Ngăn xếp đầy." if my_stack.is_full() else "Ngăn xếp không đầy.")
        elif choice == 5:
            print("Số phần tử trên ngăn xếp:", my_stack.count())
        elif choice == 6:
            my_stack.print_stack()
        elif choice == 7:
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
