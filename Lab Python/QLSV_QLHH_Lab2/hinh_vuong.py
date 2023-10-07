from hinh_chu_nhat import HinhChuNhat
class HinhVuong(HinhChuNhat):
    def __init__(self, canh: float) -> None:
        super().__init__(canh, canh)
    
    def TinhDienTich(self):
        return self.canh * self.canh
    
    def __str__(self) -> str:
        return f"Hình vuông cạnh: {self.canh} có diện tích: {self.TinhDienTich()}"

hv = HinhVuong(2)

    