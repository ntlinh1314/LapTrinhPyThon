from hinh_hoc import HinhHoc
class HinhChuNhat(HinhHoc):
    def __init__(self, ChieuDai: float, ChieuRong: float) -> None:
        super().__init__(ChieuDai)
        self.__ChieuDai = ChieuDai
        self.__ChieuRong = ChieuRong
    @property
    def ChieuDai(self):
        return self.__ChieuDai
    @property
    def ChieuRong(self):
        return self.__ChieuRong
    
    def getChieuDai(self):
        return self.ChieuDai
    def getChieuRong(self):
        return self.ChieuRong
    
    def TinhDienTich(self):
        return self.canh * self.ChieuRong
    
    def __str__(self) -> str:
        return f"Hình chữ nhật có chiều dài: {self.ChieuDai}, chiều rộng: {self.ChieuRong} có diện tích: {self.TinhDienTich()}"

hcn = HinhChuNhat(2,3)
