class HinhChuNhat:
    def __init__(self):
        self.chieu_dai = 0
        self.chieu_rong = 0

    def nhap_du_lieu(self):
        self.chieu_dai = float(input("Nhập chiều dài của hình chữ nhật: "))
        self.chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật: "))

    def tinh_chu_vi(self):
        chu_vi = 2 * (self.chieu_dai + self.chieu_rong)
        return chu_vi

    def tinh_dien_tich(self):
        dien_tich = self.chieu_dai * self.chieu_rong
        return dien_tich

    def in_thong_tin(self):
        print("Thông tin hình chữ nhật:")
        print("Chiều dài:", self.chieu_dai)
        print("Chiều rộng:", self.chieu_rong)
        print("Chu vi:", self.tinh_chu_vi())
        print("Diện tích:", self.tinh_dien_tich())

# Chương trình chính
if __name__ == "__main__":
    hcn = HinhChuNhat()
    hcn.nhap_du_lieu()
    hcn.in_thong_tin()
