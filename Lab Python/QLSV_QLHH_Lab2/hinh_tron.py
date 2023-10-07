from hinh_hoc import HinhHoc
import math
class HinhTron(HinhHoc):
    def __init__(self, BanKinh: float) -> None:
        super().__init__(BanKinh)
        self.BanKinh = BanKinh
    def TinhDienTich(self) -> float:
        return self.BanKinh ** 2 * math.pi
    def __str__(self) -> str:
        return f"Hình tròn bán kính {self.BanKinh} có diện tích là : {self.TinhDienTich()}" 
ht = HinhTron(2)
