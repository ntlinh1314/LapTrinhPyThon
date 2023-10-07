from hinh_chu_nhat import HinhChuNhat
from hinh_hoc import HinhHoc
from hinh_tron import HinhTron
from hinh_vuong import HinhVuong
from kieu_hinh import KieuHinh

class DanhSachHinhHoc:
    def __init__(self) -> None:
        self.dshh = []
        
    def themHinh(self, hh: HinhHoc):
        self.dshh.append(hh)
        
    def xuat(self):
        for hh in self.dshh:
            print(hh)
            
    def TimHinhCoDienTichLonNhat(self):
        hinhHoc = HinhHoc()
        max = 0
        for hh in self.dshh:
            if hh.TinhDienTich() > max:
                max = hh.TinhDienTich()
                hinhHoc = hh
        print(hinhHoc)
           
    def TimHinhCoDienTichNhoNhat(self):
        hinhHoc = HinhHoc()
        min = 1_000_000
        for hh in self.dshh:
            if hh.TinhDienTich() < min:
                min = hh.TinhDienTich()
                hinhHoc = hh
        print(hinhHoc)
        
    def TimHinhTronCoDienTichLonNhat(self):
        hinhHoc = HinhHoc()
        max = 0
        for hh in self.dshh:
            if isinstance(hh, HinhTron):
                if hh.TinhDienTich() > max:
                    max = hh.TinhDienTich()
                    hinhHoc = hh
        print(hinhHoc)
        
    def SapGiamTheoDienTich(self):
        return self.dshh.sort(key=lambda x:x.TinhDienTich(), reverse=True)
    
    #kieuHinh = "hinh_Tron" or "hinh_Chu_Nhat" or "hinh_Vuong" or "tat_Ca"
    def DemSoLuongKieuHinh(self, kieuHinh: str):
        kq = []
        for hh in self.dshh:
            if kieuHinh == KieuHinh.hinh_Tron.name:
                if isinstance(hh, HinhTron):
                    kq.append(hh)
            elif kieuHinh == KieuHinh.hinh_Chu_Nhat.name:
                if isinstance(hh, HinhChuNhat):
                    kq.append(hh)
            elif kieuHinh == KieuHinh.hinh_Vuong.name:
                if isinstance(hh, HinhVuong):
                    kq.append(hh)
            elif kieuHinh == KieuHinh.tat_Ca.name:
                kq.append(hh)
        print("Số lượng hình theo loại hình là: ", len(kq))
        
    def TinhTongDienTich(self):
        sum = 0
        for hh in self.dshh:
            sum += hh.TinhDienTich()
        return sum
    
    def TimHinhCoDienTichLonNhatTheoKieuHinh(self, kieuHinh: str):
        max = 0
        hinhHoc = HinhHoc()
        for hh in self.dshh:
            if kieuHinh == KieuHinh.hinh_Tron.name:
                if isinstance(hh,HinhTron):
                    if hh.TinhDienTich() > max:
                        max = hh.TinhDienTich()
                        hinhHoc = hh
            elif kieuHinh == KieuHinh.hinh_Vuong.name:
                if isinstance(hh,HinhVuong):
                    if hh.TinhDienTich() > max:
                        max = hh.TinhDienTich()
                        hinhHoc = hh
            elif kieuHinh == KieuHinh.hinh_Chu_Nhat.name:
                if isinstance(hh,HinhChuNhat):
                    if hh.TinhDienTich() > max:
                        max = hh.TinhDienTich()
                        hinhHoc = hh
            elif kieuHinh == KieuHinh.tat_Ca.name:
                if hh.TinhDienTich() > max:
                    max = hh.TinhDienTich()
                    hinhHoc = hh
        return hinhHoc
    
    def timViTriCuaHinh(self, h: HinhHoc):
        for hh in self.dshh:
            if(isinstance(hh, h) and hh.canh == h.canh):
                return hh
    
    def XuatViTri(self):
        for i in range(len(self.dshh)):
            print(f"{self.dshh[i]} : {i}")
    def XoaTaiViTri(self, viTri: int):
        for i in range(len(self.dshh)):
            if i == viTri:
                self.dshh.remove(self.dshh[i])
                return True
            else:
                return False
    
    def TimHinhTheoDTich(self, dt:float):
        hinhHoc = HinhHoc()
        for hh in self.dshh:
            if hh.TinhDienTich() == dt:
                hinhHoc = hh
        return hinhHoc
    
    def XoaHinh(self, hh:HinhHoc):
        for h in self.dshh:
            if h == hh:
                self.dshh.remove(h)
                return True
            else:
                return False
            
    def XoaHinhTheoLoai(self, kieuHinh:str):
        for hh in self.dshh:
            if kieuHinh == KieuHinh.hinh_Tron.name:
                if isinstance(hh,HinhTron):
                    self.dshh.remove(hh)
            elif kieuHinh == KieuHinh.hinh_Chu_Nhat.name:
                if isinstance(hh,HinhChuNhat):
                    self.dshh.remove(hh)
            elif kieuHinh == KieuHinh.hinh_Vuong.name:
                if isinstance(hh,HinhVuong):
                    self.dshh.remove(hh)
            else:
                self.dshh.remove(hh)
      
    def XuatHinhTheoChieuTangGiam(self, kieuHinh:str, tang:bool):
        kq = []
        for hh in self.dshh:
            if kieuHinh==KieuHinh.hinh_Tron.name:
                if isinstance(hh,HinhTron):
                    kq.append(hh)
            elif kieuHinh==KieuHinh.hinh_Chu_Nhat.name:
                if isinstance(hh,HinhChuNhat):
                    kq.append(hh)
            elif kieuHinh==KieuHinh.hinh_Vuong.name:
                if isinstance(hh,HinhVuong):
                    kq.append(hh)
            elif kieuHinh==KieuHinh.tat_Ca.name:
                kq.append(hh)
        if tang==False:
            kq.sort(key=lambda x:x.TinhDienTich(),reverse=False)
        else:
            kq.sort(key=lambda x:x.TinhDienTich(),reverse=True)
        return kq
    
    #kieuHinh = "hinh_Tron" or "hinh_Chu_Nhat" or "hinh_Vuong" or "tat_Ca"
    def TinhTongDTTheoKieuHinh(self, kieuHinh:str):
        sum =0
        for hh in self.dshh:
            if kieuHinh == KieuHinh.hinh_Tron.name:
                if isinstance(hh,HinhTron):
                    sum += hh.TinhDienTich()
            elif kieuHinh == KieuHinh.hinh_Chu_Nhat.name:
                if isinstance(hh,HinhChuNhat):
                    sum += hh.TinhDienTich()
            elif kieuHinh == KieuHinh.hinh_Vuong.name:
                if isinstance(hh,HinhVuong):
                    sum += hh.TinhDienTich()
            elif kieuHinh == KieuHinh.tat_Ca.name:
                sum += hh.TinhDienTich()
        return sum