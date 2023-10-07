from datetime import datetime
from ds_hinh_hoc import DanhSachHinhHoc
from sinh_vien import SinhVien
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sinh_vien_phi_chinh_quy import SinhVienPhiChinhQuy
from danh_sach_sv import DanhSachSinhVien
from datetime import datetime
from hinh_chu_nhat import HinhChuNhat
from hinh_hoc import HinhHoc
from hinh_tron import HinhTron
from hinh_vuong import HinhVuong
from kieu_hinh import KieuHinh

sv1 = SinhVienChinhQuy(1957690, "Trần Văn A", datetime.strptime ("23/6/1999", "%d/%m/%Y"), 80)
sv2 = SinhVienChinhQuy(1957691, "Nguyễn Văn C", datetime.strptime("5/12/1999", "%d/%m/%Y"), 90)
sv3 = SinhVienPhiChinhQuy(1957692, "Thái Thị Thu", datetime.strptime("23/6/1999", "%d/%m/%Y"), "Cao đẳng", 2)
sv4 = SinhVienPhiChinhQuy(2000324, "Trần Thanh Tâm", datetime.strptime("27/8/2000", "%d/%m/%Y"), "Cao đẳng", 2)
sv5 = SinhVienPhiChinhQuy(2004544, "Nguyễn Thanh Trà", datetime.strptime("17/5/2666", "%d/%m/%Y"), "Trung cấp", 2.5)
sv6 = SinhVienChinhQuy(1911127, "Lê Nguyễn Anh", datetime.strptime("11/12/2001", "%d/%m/%Y"), 60)

dssv = DanhSachSinhVien()
dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.themSV(sv5)
dssv.themSV(sv6)
print ("Danh sách sinh viên:")
dssv.xuat()

print ("=========")
ms=1911127
vt = dssv.TimVTSVTheoMS(ms)
print(f"SV cần tìm có vt thứ {vt + 1}")

print ("=========")
loai = "chinhquy"
for sv in dssv.TimSVTheoLoai(loai):
    print(sv)

print ("=========")    
print("Sinh viên có điểm rèn luyện 80 trở lên là: ")
for sv in dssv.TimSVCoDiemRLTren80():
    print(sv)


print ("=========")
print("Sinh viên trình độ cao đẳng và sinh trước ngày 15/8/1999 là: ")
for sv in dssv.TimSVCoTrinhDoCDVaSinhTrcNgay():
    print(sv)

ht1 = HinhTron(2)
ht2 = HinhTron(3)
ht3 = HinhTron(4)
hv1 = HinhVuong(2)
hv2 = HinhVuong(3)
hv3 = HinhVuong(4)
hcn1 = HinhChuNhat(3,2)
hcn2 = HinhChuNhat(3,4)
hcn3 = HinhChuNhat(3,5)
dshh = DanhSachHinhHoc()
dshh.themHinh(ht1)
dshh.themHinh(ht2)
dshh.themHinh(ht3)
dshh.themHinh(hv1)
dshh.themHinh(hv2)
dshh.themHinh(hv3)
dshh.themHinh(hcn1)
dshh.themHinh(hcn2)
dshh.themHinh(hcn3)

print ("=========")
print("Danh sách hình học: ")
dshh.xuat()

print ("=========")
print ("Hình có diện tích lớn nhất là:")
dshh.TimHinhCoDienTichLonNhat()

print ("=========")
print("Hình có diện tích nhỏ nhất là:")
dshh.TimHinhCoDienTichNhoNhat()

print ("=========")
print ("Hình tròn có diện tích lớn nhất là:")
dshh.TimHinhTronCoDienTichLonNhat()

print ("=========")
print ("Sắp giảm theo diện tích:")
dshh.SapGiamTheoDienTich()
dshh.xuat()

print ("=========")
print("Đếm")
dshh.DemSoLuongKieuHinh("tat_Ca")

print ("=========")
print("Tổng diện tích")
print(dshh.TinhTongDienTich())

print("=====")
print(dshh.TimHinhCoDienTichLonNhatTheoKieuHinh("hinh_Vuong"))

print("====")
print(dshh.timViTriCuaHinh(HinhVuong))
print("==Vi tri===")
dshh.XuatViTri()

print("=====")
if dshh.XoaTaiViTri(7) == False:
    print("True")
else:
    print("False")


print("=====")
#dshh.XoaHinhTheoLoai("hinh_Chu_Nhat")
for i in dshh.XoaHinhTheoLoai("hinh_Chu_Nhat"):
    print(i)

print("======")
for i in dshh.XuatHinhTheoChieuTangGiam("tat_Ca",False):
    print(i)

print ("=========")   
print("TinhTong")
print(dshh.TinhTongDTTheoKieuHinh("hinh_Chu_Nhat"))