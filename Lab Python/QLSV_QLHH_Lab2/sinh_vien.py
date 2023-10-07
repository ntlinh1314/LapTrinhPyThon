from datetime import datetime


class SinhVien:
    truong = "Đại học Đà Lạt"
    
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.maSo = maSo
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh
        
    @property
    def hoTen(self):
        return self._hoTen
    @hoTen.setter
    def hoTen(self, hoTen:str):
        self._hoTen = hoTen
    
    @staticmethod
    def laMaSoHopLe(mssv:int):
        return len(str(mssv))==7
    def __str__(self) -> str:
        return f"{self.maSo}\t{self.hoTen}\t{self.ngaySinh}"