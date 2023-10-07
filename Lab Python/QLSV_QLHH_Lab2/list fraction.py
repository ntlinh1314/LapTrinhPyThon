from PhanSo import PhanSo

class DanhSachPhanSo:
    def __init__(self) -> None:
        self.listfraction = []
        
    def themPS(self, ps: PhanSo):
        self.listfraction.append(ps)
        
    def xuat(self):
        for ps in self.listfraction:
            print(ps, end= " ")

    def demPSAm(self):
        count = 0
        for ps in self.listfraction:
            if ps.tu * ps.mau < 0:
                count += 1
        print("Số phân số âm là: ", count)

     
    
    def demPSAm(self):
        am_numbers = []
        for ps in self.listfraction:
            if ps.tu * ps.mau < 0:
                am_numbers.append(ps)
        print("Số phân số âm là: ", len(am_numbers))
        print("Các phân số âm là:")
        for ps in am_numbers:
            print(ps)
        
       
    def TimPSDuongNhoNhat(self):
        _min  = PhanSo(1_000_000_000)
        for ps in self.listfraction:
            if ps.tu*ps.mau > 0 and ps < _min:
                _min = ps
        print ("Phân số dương nhỏ nhất là: ", _min)
    
    '''def TimViTri(self):
        for i in range(len(self.listfraction)):
            print(f"{self.listfraction[i]} có vị trí: ", i+1)'''
    
    def TimViTriCuaPS(self, ps:PhanSo) -> int:
        for i in range(len(self.listfraction)):
            if self.listfraction[i]==ps:
                return i
        return -1
    
    def TongPSAm(self):
        _sum = PhanSo()
        for ps in self.listfraction:
            if ps.tu * ps.mau < 0:
                _sum = _sum + ps
        print(f"{_sum.tu} / {_sum.mau}")
    
    def XoaPS(self, ps):
        vt = self.TimViTriCuaPS(ps)
        if vt >= 0:
            del self.listfraction[vt]
            return True
        else:
            return False
        
    def XoaPSTheoTu(self,tu:int):
        for ps in self.listfraction:
            if ps.tu == tu:
                self.listfraction.remove(ps)
        
    def SortPSTangTheoTu(self):
        sort = self.listfraction.sort(key=lambda x:x.tu)
        print(sort)
        self.xuat()
    def SortPSTangTheoMau(self):
        sort = self.listfraction.sort(key=lambda x:x.mau)
        print(sort)
        self.xuat()
    def SortPSGiamTheoTu(self):
        sort = self.listfraction.sort(key=lambda x:x.tu,reverse=True)
        print(sort)
        self.xuat()
    def SortPSGiamTheoMau(self):
        sort = self.listfraction.sort(key=lambda x:x.mau,reverse=True)
        print(sort)
        self.xuat()
dsps = DanhSachPhanSo()   
fr = open("E:\\Lưu bài Python\Python_Lip\dsps.txt", "r")

for f in fr:
    tu = int(f.split(" ")[0])
    mau = int(f.split(" ")[1])
    ps = PhanSo(tu, mau)
    dsps.themPS(ps)

print("ds")
dsps.xuat()
dsps.demPSAm()
dsps.TimPSDuongNhoNhat()
#dsps.TimViTri()
dsps.TongPSAm()
ps = PhanSo(1,5)
vt = dsps.TimViTriCuaPS(ps)
if vt >=1:
    print(f"{ps.tu} / {ps.mau} co vt {vt+1}")
else:
    print("fail")
if dsps.XoaPS(ps) == True:
    print("Xóa thành công")
else:
    print("Delete thất bại")

tu = -1
dsps.XoaPSTheoTu(tu)
dsps.xuat()

