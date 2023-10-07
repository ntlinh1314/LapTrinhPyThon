import tkinter as tk
import tkinter.simpledialog
import tkinter.messagebox
import tkinter.filedialog
from subprocess import CompletedProcess

from Project import *


class TkApp(tk.Tk):
    def __init__(self, title = 'Server Management App', geometry = '360x480', file = 'menu.txt', **kwargs) -> None:
        # Create root window
        super().__init__(**kwargs)
        # Set title
        self.title(title)
        # Set geometry
        self.geometry(geometry)
        # Create menu
        self.__add_menu(file)

    def run(self) -> None:
        self.mainloop()

    def __add_menu(self, file: str) -> None:
        menu = tk.Frame(self)
        menu.pack()
        label = tk.Label(menu, text = self.title(), font = ('Arial', 22))
        label.grid(row = 0, sticky = 'nesw')
        # Read button labels from file
        with open(file,'r') as f:
            i = 1
            for line in f.readlines():
                # Each button corresponds to a choice in __handle_button()
                button = tk.Button(menu, text = line.strip(), command = lambda chon = i: self.__handle_button(chon))
                # Places button in menu using grid(), with kwarg sticky = 'nesw' to have button expand in size to fully fit the parent
                button.grid(row = i, sticky = 'nesw', padx = 4, pady = 4)
                i += 1
            f.close()

    def __evaluate_command(self, command: CompletedProcess) -> None:
        if command is None:
            return
        if command.returncode == 0:
            tk.messagebox.showinfo("Thanh cong", "Lenh chay thanh cong!")
        else:
            tk.messagebox.showerror("Error", command.stderr)

    def __handle_button(self, chon: int) -> None:
        match chon:
            case 1:
                # Create dialog to ask for input from user
                username = tk.simpledialog.askstring("Nhap ten user", "Nhap ten user: ")
                # End the sequence if the user presses 'Cancel'
                # Co the can chuc nang ben kia tra ve bool thuc hien lenh thanh cong khong de the hien o giao dien
                if username is None:
                    return
                password = tk.simpledialog.askstring("Nhap mat khau", "Nhap mat khau: ")
                if password is None:
                    return
                ou = tk.simpledialog.askstring("Nhap Ou Con", "Nhap Ou Con: ")
                if ou is None:
                    return
                ou1 = tk.simpledialog.askstring("Nhap Ou Cha", "Nhap Ou Cha: ")
                if ou is None:
                    return
                domain = "dc=hihi,dc=com"
                self.__evaluate_command(createUser(splitName(username), password, ou, ou1, domain))
            case 2:
                username = tk.simpledialog.askstring("Nhap ten user", "Nhap ten user: ")
                if username is None:
                    return
                newpassword = tk.simpledialog.askstring("Nhap mat khau moi", "Nhap mat khau moi: ")
                if newpassword is None:
                    return
                ou1 = tk.simpledialog.askstring("Nhap OU Con", "Nhap OU Con: ")
                if ou1 is None:
                    return
                ou2 = tk.simpledialog.askstring("Nhap OU Cha", "Nhap OU Cha: ")
                if ou2 is None:
                    return
                domain = "dc=hihi,dc=com"
                self.__evaluate_command(changePass(splitName(username), newpassword, ou1, ou2, domain))
            case 3:
                username = tk.simpledialog.askstring("Nhap ten user", "Nhap ten user: ")
                if username is None:
                    return
                ou1 = tk.simpledialog.askstring("Nhap OU Con", "Nhap OU Con: ")
                if ou1 is None:
                    return
                ou2 = tk.simpledialog.askstring("Nhap OU Cha", "Nhap OU Cha: ")
                if ou2 is None:
                    return
                domain = "dc=hihi,dc=com"
                ipServer = tk.simpledialog.askstring("Nhap IP cua Server", "Nhap IP cua Server: ")
                nameFolder = tk.simpledialog.askstring("Nhap ten thu muc muon tao Profile", "Nhap ten thu muc muon tao Profile: ")
                password = tk.simpledialog.askstring("Nhap password", "Nhap password: ")
                self.__evaluate_command(createProfile(splitName(username), ou1, ou2, domain, ipServer, nameFolder, password))
            case 4:
                self.__evaluate_command(installService())
            case 5:
                userdel = tk.simpledialog.askstring("Nhap user muon xoa", "Nhap user muon xoa: ")
                if userdel is None:
                    return
                ou1 = tk.simpledialog.askstring("Nhap OU Con", "Nhap OU Con: ")
                if ou1 is None:
                    return
                ou2 = tk.simpledialog.askstring("Nhap OU Cha", "Nhap OU Cha: ")
                if ou2 is None:
                    return
                domain ="dc=hihi,dc=com"
                self.__evaluate_command(removeUser(splitName(userdel), ou1, ou2, domain))
            case 6:
                # Create dialog to ask to open file
                filename = tk.filedialog.askopenfilename()
                # Check if filename (a tuple) is empty (user pressed Cancel)
                if not filename:
                    return
                self.__evaluate_command(readCSVFile(filename))
            case 7:
                removeService()
            case 8:
                username = tk.simpledialog.askstring("Nhap username", "Nhap username: ")
                if username is None:
                    return
                self.__evaluate_command(addUsertoRemoteDesktop(splitName(username)))
            case 9:
                ou = tk.simpledialog.askstring("Nhap OU muon tao", "Nhap OU muon tao: ")
                domain = "dc=hihi,dc=com"
                self.__evaluate_command(createOuParent(ou, domain))
            case 10:
                ou1 = tk.simpledialog.askstring("Nhap OU muon tao", "Nhap OU muon tao: ")
                ou2 = tk.simpledialog.askstring("Nhap OU cha", "Nhap OU cha: ")
                domain = "dc=hihi,dc=com"
                self.__evaluate_command(createOuChild(ou1, ou2, domain))
            
            case _:
                # End the program
                self.destroy()


if __name__ == '__main__':
    app = TkApp(title = 'Server Management App', geometry = '600x800', file = 'menu.txt')
    app.run()
