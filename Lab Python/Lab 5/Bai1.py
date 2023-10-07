import sqlite3

def get_connection():
    connection = sqlite3.connect("E:\Lưu bài Python\Lab 5\Lab5.db")
    return connection

def close_connection(conection):
    if conection:
        conection.close()

def get_all_class():
    try:  
        conection = get_connection()
        cursor = conection.cursor()
        query = "SELECT * FROM Lop"
        cursor.execute(query)
        ds = cursor.fetchall()
        print(f"Danh sách các lớp là: ")
        for row in ds:
            print("+"*50)
            print("Mã lớp: ",row[0])
            print("Tên lớp: ",row[1]) 
            print("+"*50)
        close_connection(conection)
    except (Exception, sqlite3.Error) as error:
        print("Đã có lỗi xảy ra. Thông tin lỗi: ",error)
get_all_class()

def get_all_sv():
    try:  
        conection = get_connection()
        cursor = conection.cursor()
        query = "SELECT * FROM SinhVien"
        cursor.execute(query)
        ds = cursor.fetchall()
        print(f"Danh sách tất cả sinh viên là: ")
        print(f"Mã số\t\tHọ tên\t\t\tMã lớp")
        for row in ds:
            print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}")
        close_connection(conection)
    except (Exception, sqlite3.Error) as error:
        print("Đã có lỗi xảy ra. Thông tin lỗi: ",error)
get_all_sv()

def get_sv_by_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query ="SELECT sv.ID, sv.HoTen, l.TenLop FROM SinhVien sv, Lop l WHERE l.ID = sv.MaLop"
        cursor.execute(query)
        records = cursor.fetchall()
        print("Danh sách tất cả sinh viên là: ")
        for row in records:
            print(f"{row[0]}\t\t\t{row[1]}\t\t\t{row[2]}")
    except (Exception, sqlite3.Error) as error:
        print("Đã có lỗi xảy ra. Thông tin lỗi: ",error)
get_sv_by_class()

def get_class_by_id(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Lop WHERE ID = ?", (class_id))
        records = cursor.fetchone()
        print(f"Thông tin lớp có id = {class_id} là: ")
        print("Mã lớp: ", records[0])
        print("Tên lớp: ", records[1])
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Đã có lỗi xảy ra. Thông tin lỗi: ",error)
get_class_by_id("1")

def insert_class(class_name):
    try:
        conection = get_connection()
        cursor = conection.cursor()
        query = "INSERT INTO Lop(TenLop) values (?)"
        cursor.execute(query,(class_name,))
        conection.commit()
        print("Success")
        close_connection(conection)
    except (Exception, sqlite3.Error) as error:
        print("Đã có lỗi xảy ra. Thông tin lỗi: ",error) 
insert_class("CTK47_MMT")

def insert_sv(sv_name,sv_class):
    try:
        conection = get_connection()
        cursor = conection.cursor()
        query = "INSERT INTO SinhVien(HoTen, MaLop) values (?, ?)"
        cursor.execute(query,(sv_name,sv_class,))
        conection.commit()
        print("Success")
        close_connection(conection)
    except (Exception, sqlite3.Error) as error:
        print("Đã có lỗi xảy ra. Thông tin lỗi: ",error)
insert_sv("Nguyen Nhat Linh","5")

def update_sv(sv_name,sv_class):
    try:
        conection = get_connection()
        cursor = conection.cursor()
        query = "UPDATE SinhVien set HoTen=?, MaLop=?"
        cursor.execute(query,(sv_name,sv_class,))
        conection.commit()
        print("Success")
        close_connection(conection)
    except (Exception, sqlite3.Error) as error:
        print("Đã có lỗi xảy ra. Thông tin lỗi: ",error)
update_sv("Nguyen Nhat Truong","5")

def delete_sv(sv_name):
    try:
        conection = get_connection()
        cursor = conection.cursor()
        query = "DELETE FROM KhachHang WHERE HoTen=?"
        cursor.execute(query,(sv_name,))
        conection.commit()
        print("Success")
        close_connection(conection)
    except (Exception, sqlite3.Error) as error:
        print("Đã có lỗi xảy ra. Thông tin lỗi: ",error)