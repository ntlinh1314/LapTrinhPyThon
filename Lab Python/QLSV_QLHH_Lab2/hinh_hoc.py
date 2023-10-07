class HinhHoc:
    def __init__(self, canh=0.0) -> None:
        self.__canh = canh
    @property
    def canh(self):
        return self.__canh
    
    def TinhDienTich(self) -> float:
        pass
    
    def __str__(self) -> str: 
        return f"{self.canh}"
   
hh = HinhHoc()    