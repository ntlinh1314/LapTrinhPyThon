from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import sqlite3

class MonAn:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý Món Ăn")
        self.root.geometry("1280x460+120+255")
        self.root.resizable(False,False)
    
        #variable
        self.var_ms=StringVar()
        self.var_ten=StringVar()
        self.var_donvitinh=StringVar()
        self.var_dongia=StringVar()
        self.var_nhom=StringVar()
        #LableFrame
        lableframeLeft = LabelFrame(self.root,bd=2,relief=RIDGE,text="Thông tin món ăn",padx=2)
        lableframeLeft.place(x=5,y=50,width=425,height=400)
        #Lable and Entry
        ms_lb = Label(lableframeLeft,text="Mã số",padx=2,pady=6).grid(row=0,column=0,sticky=W)
        ms_entry = Entry(lableframeLeft,width=40,textvariable=self.var_ms).grid(row=0,column=1)

        ten_lb = Label(lableframeLeft,text="Tên món",padx=2,pady=6).grid(row=1,column=0,sticky=W)
        ten_entry = Entry(lableframeLeft,width=40,textvariable=self.var_ten).grid(row=1,column=1)

        dvt_lb = Label(lableframeLeft,text="Đơn vị tính",padx=2,pady=6).grid(row=2,column=0,sticky=W)
        dvt_entry = Entry(lableframeLeft,width=40,textvariable=self.var_donvitinh).grid(row=2,column=1)

        nhom_lb = Label(lableframeLeft,text="Nhóm",padx=2,pady=6).grid(row=3,column=0,sticky=W)
        nhom_cbb = Combobox(lableframeLeft,width=37,textvariable=self.var_nhom,state="readonly")
        nhom_cbb["value"]=("1","2","3","4")
        nhom_cbb.current(0)
        nhom_cbb.grid(row=3,column=1)

        gia_lb = Label(lableframeLeft,text="Giá",padx=2,pady=6).grid(row=4,column=0,sticky=W)
        gia_entry = Entry(lableframeLeft,width=40,textvariable=self.var_dongia).grid(row=4,column=1)
        #button
        buttonFrame = Frame(lableframeLeft,bd=2,relief=RIDGE)
        buttonFrame.place(x=0,y=220,width=415,height=125)

        btn_them = Button(buttonFrame, text="Thêm",bg="#b0d46c",width=20,command=self.them_data)
        btn_them.grid(row=0,column=0,padx=30,pady=20)

        btn_luu = Button(buttonFrame, text="Lưu",bg="#b0d46c",width=20,command=self.capNhat_data)
        btn_luu.grid(row=1,column=0,padx=30,pady=20)

        btn_xoa = Button(buttonFrame, text="Xoá",bg="#b0d46c",width=20,command=self.xoa_data)
        btn_xoa.grid(row=0,column=1,padx=30,pady=20)

        btn_reset = Button(buttonFrame, text="F5",bg="#b0d46c",width=20,command=self.reset)
        btn_reset.grid(row=1,column=1,padx=30,pady=20)

        #tableframe
        tableFrame = LabelFrame(self.root,bd=2,relief=RIDGE,text="Bảng thông tin",padx=2)
        tableFrame.place(x=435,y=50,width=840,height=400)

        timKiem_lb = Label(tableFrame,text="Tìm kiếm theo: ",padx=2,pady=6).grid(row=0,column=0,sticky=W)

        self.search_var = StringVar()
        timKiem_cbb = Combobox(tableFrame,width=20,state="readonly",textvariable=self.search_var)
        timKiem_cbb["value"]=("TenMonAn","Nhom")
        timKiem_cbb.current(0)
        timKiem_cbb.grid(row=0,column=1)
        self.search_txt = StringVar()
        timKiem_entry = Entry(tableFrame,width=53,textvariable=self.search_txt).grid(row=0,column=2,padx=3)

        btn_timKiem = Button(tableFrame, text="Tìm",bg="#b0d46c",width=10,command=self.search)
        btn_timKiem.grid(row=0,column=3,padx=10,pady=20)
        btn_resetTK = Button(tableFrame, text="F5",bg="#b0d46c",width=10,command=self.ThongTinData)
        btn_resetTK.grid(row=0,column=4,padx=10,pady=20)
        
        #dataTable
        dataTableFrame = Frame(tableFrame,bd=2,relief=RIDGE)
        dataTableFrame.place(x=0,y=70,width=830,height=305) 

        scrollx = Scrollbar(dataTableFrame,orient=HORIZONTAL)
        scrolly = Scrollbar(dataTableFrame,orient=VERTICAL)

        self.BangMonAn=Treeview(dataTableFrame,columns=("MaMonAn","TenMonAn","DonViTinh","DonGia","Nhom"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.BangMonAn.xview)
        scrolly.config(command=self.BangMonAn.yview)

        self.BangMonAn.heading("MaMonAn",text="Mã món")
        self.BangMonAn.heading("TenMonAn",text="Tên món")
        self.BangMonAn.heading("DonViTinh",text="Đơn vị")
        self.BangMonAn.heading("Nhom",text="Nhóm")
        self.BangMonAn.heading("DonGia",text="Giá")

        self.BangMonAn["show"]="headings"
        self.BangMonAn.pack(fill=BOTH,expand=1)
        self.BangMonAn.bind("<ButtonRelease-1>",self.LayDuLieu)
        self.ThongTinData()

    def them_data(self):
        conn=sqlite3.connect("E:\Lưu bài Python\Lab 5\Lab5.db", timeout=20)
        if (self.var_ten.get()=="" or self.var_donvitinh.get()=="") and (self.var_dongia.get()=="" or self.var_ms.get()=="" ):
            messagebox.showerror("Error","Phải điền đầy đủ thông tin!",parent=self.root)
        else:
            try:
                myCursor = conn.cursor()
                kh = (
                    self.var_ms.get(),
                self.var_ten.get(),
                self.var_donvitinh.get(),
                self.var_dongia.get(),
                self.var_nhom.get()
                )
                data_insert = f"""INSERT INTO MonAn (MaMonAn,TenMonAn,DonViTinh,DonGia,Nhom) VALUES (?,?,?,?,?)"""
                myCursor.execute(data_insert,kh)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Đã thêm thành công món ăn!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Có sự cố đã xảy ra {str(es)}",parent=self.root)

    def ThongTinData(self):
        conn=sqlite3.connect("E:\Lưu bài Python\Lab 5\Lab5.db", timeout=20) 
        myCursor = conn.execute("""SELECT * FROM MonAn""")
        fetch = myCursor.fetchall()
        if len(fetch)!=0:
            self.BangMonAn.delete(*self.BangMonAn.get_children())
            for i in fetch:
                self.BangMonAn.insert('','end',values=(i))
            conn.close()
        conn.close()

    def capNhat_data(self):
        conn=sqlite3.connect("E:\Lưu bài Python\Lab 5\Lab5.db", timeout=20)
        myCursor = conn.cursor()
        kh = (
                    self.var_ms.get(),
                self.var_ten.get(),
                self.var_donvitinh.get(),
                self.var_dongia.get(),
                self.var_nhom.get(),
                self.var_ms.get()
                )
        data_update = """UPDATE MonAn SET MaMonAn=?,TenMonAn=?,DonViTinh=?,DonGia=?,Nhom=? WHERE MaMonAn=?"""
        myCursor.execute(data_update,kh)
        conn.commit()
        self.LayDuLieu()
        conn.close()
        messagebox.showinfo("Update","Cap nhat thanh cong!",parent=self.root)

    def xoa_data(self):
        tbXoa = messagebox.askyesno("He thong","Ban co muon xoa mon an nay",parent=self.root)
        if tbXoa > 0:
            conn=sqlite3.connect("E:\Lưu bài Python\Lab 5\Lab5.db", timeout=20)
            myCursor = conn.cursor()
            kh = (
                self.var_ms.get()
            )
            data_delete = "DELETE FROM MonAn WHERE MaMonAn=?"
            messagebox.showinfo("Thong bao","Da xoa mon an thanh cong")
            myCursor.execute(data_delete,kh)
            conn.commit()
            self.LayDuLieu()
            conn.close()

    def reset(self):
        self.var_ms.set(""),
        self.var_ten.set(""),
        self.var_donvitinh.set(""),
        self.var_dongia.set("")     

    def LayDuLieu(self,envent=""):
        hang = self.BangMonAn.focus()
        content = self.BangMonAn.item(hang)
        row = content["values"]
        self.var_ms.set(row[0]),
        self.var_ten.set(row[1]),
        self.var_donvitinh.set(row[2]),
        self.var_dongia.set(row[3]),
        self.var_nhom.set(row[4])

    def search(self):
        conn=sqlite3.connect("E:\Lưu bài Python\Lab 5\Lab5.db", timeout=20)
        myCursor = conn.cursor()
        query = "SELECT * FROM MonAn WHERE "+str(self.search_var.get())+" LIKE '%"+str(self.search_txt.get())+"%'"
        print(query)
        myCursor.execute(query)
        fetch = myCursor.fetchall()
        if len(fetch) !=0:
            self.BangMonAn.delete(*self.BangMonAn.get_children())
            for i in fetch:
                self.BangMonAn.insert("",'end',values=(i))
            conn.commit()
        conn.close()
        
if __name__ == "__main__":
    root = Tk()
    obj = MonAn(root)
    root.mainloop() 