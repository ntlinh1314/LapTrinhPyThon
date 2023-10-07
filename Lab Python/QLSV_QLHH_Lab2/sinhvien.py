from codecs import utf_8_encode
from datetime import date, datetime


class SinhVien:
    #Biến của lớp
    truong = "Đại học Đà Lạt"
    
    #Hàm khởi tạo, hàm tạo lập: khởi gán các thuộc tính của đối tượng
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo #thuộc tính private
        self.__hoTen = hoTen #thuộc tính private
        self.__ngaySinh = ngaySinh #thuộc tính private
    
    # cho phép truy xuất tới thuộc tính từ bên ngoài thông qua trường maSo
    @property
    def maSo(self):
        return self.__maSo
    
    @property
    def hoTen(self):
        return self.__hoTen
    
    @property
    def ngaySinh(self):
        return self.__ngaySinh
    
    # cho phép thay đổi giá trị của thuộc tính maSo
    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.maSo == maso
    
    # phương thức tỉnh: các phương thức không truy xuất gì đến thuộc tỉnh, hành vi của lớp
    # những phương thức này không cần truyền tham số mặc định self
    # đây không phải là một hành vi (phương thức) của 1 đối tượng thuộc lớp
    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7
    
    # phương thức của lớp, chỉ truy xuất tới các biến thành viên của lớp
    # không truy xuất được các thuộc tỉnh riêng của đôi tượng
    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi
    
    # tương tự ghi đè phương thức toString()
    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    
    # hành vi của đối tượng sinh viên
    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")
class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []
    
    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)
    
    def xuat(self):
        for sv in self.dssv:
            print(sv)
    
    # Tìm sv theo mã số
    def timSVTheoMS(self, ms: int) -> list:
        return [sv for sv in self.dssv if sv.maSo == ms]
    
    # Tìm vị trí của SV
    def timVTSVTheoMS(self, ms:int) -> int:
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == ms:
                return i
        return -1
    
    # Xóa sinh viên có mssv, thông báo xóa đc hay k
    def xoaSV(self, ms):
        vt = self.timVTSVTheoMS(ms)
        if vt >= 0:
            del self.dssv[vt]
            return True
        else:
            return False
        
    # Tìm sinh viên tên Nam
    def timSVTheoTen(self, name: str) -> list:
        #return [sv for sv in self.dssv if sv.hoTen.split(' ')[-1] == name]
        kq = []
        for i in range(len(self.dssv)):
            if self.dssv[i].hoTen.split(' ')[-1] == name:
                kq.append(self.dssv[i])
        return kq
    # Tìm những sinh viên sinh trước 15/6/2000
    def timSVTruocNgaySinh(self, date:datetime) -> list:
        #return [sv for sv in self.dssv if sv.ngaySinh < date]
        kq = []
        for i in range(len(self.dssv)):
            if self.dssv[i].ngaySinh < date:
                kq.append(self.dssv[i])
        return kq

    def hoTenSV(self):
        return self.hoTen
    #Sắp xếp dssv theo chiều tăng:
    def sortSVTang(self):
        sort = self.dssv.sort(key=lambda ht:ht.hoTen.split(" ")[-1])
        return sort
                
    #Sắp xếp dssv theo chiều giảm:
    def sortSVGiam(self):
        sort = self.dssv.sort(key=lambda ht:ht.hoTen.split(" ")[-1],reverse=True)
        return sort
    
sv1 = SinhVien(1234,"A",datetime.strptime("1/2/2001", "%d/%m/%Y"))
sv2 = SinhVien(1235,"AB",datetime.strptime("1/2/2001", "%d/%m/%Y"))
sv3 = SinhVien(1236,"ABC",datetime.strptime("1/2/2000", "%d/%m/%Y"))
sv4 = SinhVien(1237,"Nam",datetime.strptime("1/2/2000", "%d/%m/%Y"))
dssv = DanhSachSV()
dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.xuat()
ms = 1234
for sv in dssv.timSVTheoMS(ms):
    print(f'{sv} co ms {ms}')

vt = dssv.timVTSVTheoMS(ms)
if vt >= 0:
    print(f'ms {ms} co vt {vt + 1}')
else:
    print('nguoc lai')

if dssv.xoaSV(ms) == True:
    print(f'Xóa thành công sinh viên có mã số {ms}')
    dssv.xuat()
else:
    print('Failure')



date = datetime.strptime("15/6/2000","%d/%m/%Y")
print(f'Danh sách sinh viên có ngày sinh trước {date} là: ')
for sv in dssv.timSVTruocNgaySinh(date):
    print(sv)


# list = []
# for i in f.readlines():    
#     list.append(i)
# print(list)
# listsort = []
# for sv in list:
#     listsort.append(sv.split(" "))
# #Sắp xếp tăng theo tên
# sort = sorted(listsort, key = lambda sv:sv[-1])
# print(sort) 
# #Sắp xếp giảm theo tên
# sort = sorted(listsort, key = lambda sv:sv[-1], reverse=True)
# print(sort) 
f = open("E:\\Lưu bài Python\Python_Lip\dssv.txt", "r")
for i in f:
    maSo = i.split('\t')[0]
    hoTen = i.split('\t')[1]
    ngaySinh = i.split('\t')[2].strip()
    ngaySinh = datetime.strptime(ngaySinh, "%d/%m/%Y")
    sinhdiên = SinhVien(maSo, hoTen, ngaySinh)
    dssv.themSV(sinhdiên)
dssv.xuat()
name = "Nam"
for sv in dssv.timSVTheoTen(name):
    print(f'Danh sách sinh viên kiếm theo tên là: \n{sv}')
dssv.sortSVTang()
print('Sắp xếp danh sách sinh viên tăng theo họ tên: ')
dssv.xuat()
dssv.sortSVGiam()
print('Sắp xếp danh sách sinh viên giảm theo họ tên: ')
dssv.xuat()
