class ThíSinh:
    def __init__(self):
        self.ho_ten = ""
        self.diem_toan = 0
        self.diem_ly = 0
        self.diem_hoa = 0

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên của thí sinh: ")
        self.diem_toan = float(input("Nhập điểm môn Toán: "))
        self.diem_ly = float(input("Nhập điểm môn Lý: "))
        self.diem_hoa = float(input("Nhập điểm môn Hoá: "))

    def in_thong_tin(self):
        print("Họ tên:", self.ho_ten)
        print("Điểm môn Toán:", self.diem_toan)
        print("Điểm môn Lý:", self.diem_ly)
        print("Điểm môn Hoá:", self.diem_hoa)

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

# Chương trình chính
if __name__ == "__main__":
    danh_sach_thi_sinh = []
    so_luong_thi_sinh = int(input("Nhập số lượng thí sinh: "))

    for i in range(so_luong_thi_sinh):
        thi_sinh = ThíSinh()
        thi_sinh.nhap_thong_tin()
        danh_sach_thi_sinh.append(thi_sinh)

    diem_chuan = 20

    # Sắp xếp danh sách thí sinh theo tổng điểm giảm dần
    danh_sach_thi_sinh.sort(key=lambda x: x.tinh_tong_diem(), reverse=True)

    print("Danh sách thí sinh trúng tuyển:")
    for thi_sinh in danh_sach_thi_sinh:
        if thi_sinh.tinh_tong_diem() >= diem_chuan:
            thi_sinh.in_thong_tin()
            print("Tổng điểm:", thi_sinh.tinh_tong_diem())



