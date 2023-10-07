from datetime import datetime
from sinh_vien import SinhVien
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sinh_vien_phi_chinh_quy import SinhVienPhiChinhQuy

class DanhSachSinhVien:
    def __init__(self) -> None:
        self.dssv = []
    def themSV(self, sv:SinhVien):
            self.dssv.append(sv)
    def xuat(self):
        for sv in self.dssv:
            print(sv)
    def TimSVTheoMS(self, ms:str):
        return [sv for sv in self.dssv if sv.maSo == ms]
    
    def TimSVTheoLoai(self, loai:str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        else:
            return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiChinhQuy)]
        
    def TimVTSVTheoMS(self, ms:int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == ms:
                return i
        return -1
    #Tìm sinh viên có điểm rèn luyện từ 80 trở lên
    def TimSVCoDiemRLTren80(self):
        kq = []
        for sv in self.dssv:
            if isinstance(sv, SinhVienChinhQuy):
                if sv.diemRL >= 80:
                    kq.append(sv)
        return kq
    
    #Tìm sinh viên có trình độ cao đẳng sinh trước 15/8/1999
    def TimSVCoTrinhDoCDVaSinhTrcNgay(self):
        kq = []
        ngay = datetime.strptime("15/8/1999","%d/%m/%Y")
        trinhDo = "Cao đẳng"
        for sv in self.dssv:
            if isinstance(sv, SinhVienPhiChinhQuy):
                if sv.trinhDo == trinhDo and sv.ngaySinh < ngay:
                    kq.append(sv)
        return kq

dssv = DanhSachSinhVien()
