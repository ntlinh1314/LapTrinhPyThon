import math

class PhanSo:
    def __init__(self, tu=0, mau=1) -> None:
        self.tu = tu
        self.mau = mau
        self.rutGon()
    def rutGon(self):
        uc = math.gcd(int(self.tu), int(self.mau))
        self.tu = self.tu//uc
        self.mau = self.mau//uc
    def __add__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau + self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq
    def __sub__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau - self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __mul__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __truediv__(self, other):
        if other.tu == 0:
            raise ArithmeticError("Mẫu số k đc <= 0.")
        kq = PhanSo()
        kq.tu = self.tu * other.mau 
        kq.mau = self.mau * other.tu
        kq.rutGon()
        return kq
    
    def __eq__(self, other):
        return self.tu * other.mau == self.mau * other.tu
    
    def __gt__(self, other):
        return (self.tu / self.mau) > (other.tu / other.mau)

    def __lt__(self, other):
        return (self.tu / self.mau) < (other.tu / other.mau)
    
    def xuat(self):
        print(self.tu, "/", self.mau)
        
    def __str__(self) -> str:
        return f"{self.tu}/{self.mau}"
    def laPhanSoAm(self):
        return self.tu*self.mau < 0

f1= PhanSo(1,2)
f2 = PhanSo(3,4)
print(f"{f1} + {f2} = {f1+f2}")
print(f"{f1} - {f2} = {f1-f2}")
print(f"{f1} * {f2} = {f1*f2}")
print(f"{f1} / {f2} = {f1/f2}")
print(f1 == f2)
