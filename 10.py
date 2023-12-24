import json
from datetime import datetime

def save_to_json(transactions):
    current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    file_name = f"{current_datetime}.json"

    data_to_save = {
        "datetime": current_datetime,
        "transactions": transactions
    }

    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data_to_save, file, indent=2)

def display_menu():
    print("----- Quản lý giao dịch -----")
    print("1. Thêm giao dịch tiền")
    print("2. Thêm giao dịch vàng")
    print("3. Hiển thị tất cả giao dịch")
    print("0. Kết thúc")

def main():
    transactions = []

    while True:
        display_menu()
        choice = input("Chọn thao tác (0-3): ")

        if choice == '1':
            amount = float(input("Nhập số tiền: "))
            transactions.append({"type": "Tiền", "amount": amount})
        elif choice == '2':
            gold_weight = float(input("Nhập khối lượng vàng: "))
            transactions.append({"type": "Vàng", "gold_weight": gold_weight})
        elif choice == '3':
            print("----- Tất cả giao dịch -----")
            for transaction in transactions:
                print(transaction)
        elif choice == '0':
            save_choice = input("Bạn có muốn ghi vào tệp tin JSON không? (1: Có, 0: Không): ")
            if save_choice == '1':
                save_to_json(transactions)
                print("Dữ liệu đã được ghi vào tệp tin JSON.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
