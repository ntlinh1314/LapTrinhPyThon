import os
import csv
from subprocess import Popen,PIPE
import shlex
import subprocess

def createUser(username, password, ou,ou1, domain):
    command="dsadd user "+ chr(34)+"cn="+username+",ou="+ou+","+"ou="+ou1+","+domain+chr(34)+" -pwd "+password
    print(command)
    #os.system(command)
    return subprocess.run(shlex.split(command),capture_output=True)

def createOuParent(ou,domain):
    command="dsadd ou "+ chr(34)+"ou="+ou+","+domain+chr(34)
    print(command)
    #os.system(command)
    return subprocess.run(shlex.split(command),capture_output=True)

def createOuChild(ou1,ou2,domain):
    command="dsadd ou "+ chr(34)+"ou="+ou1+","+"ou="+ou2+","+domain+chr(34)
    print(command)
    #os.system(command)
    return subprocess.run(shlex.split(command),capture_output=True)

def changePass(username,password,ou1,ou2,domain):
    command="dsmod user "+ chr(34)+"cn="+username+",ou="+ou1+","+"ou="+ou2+","+domain+chr(34)+" -pwd "+password
    print(command)
    #os.system(command)
    return subprocess.run(shlex.split(command),capture_output=True)

def removeUser(username,ou1,ou2,domain):
    domain="dc=hihi,dc=com"
    command = "dsrm -noprompt "+chr(34)+"cn="+username+",ou="+ou1+",ou="+ou2+","+domain+chr(34)
    print(command)
    #os.system(command)
    return subprocess.run(shlex.split(command),capture_output=True)

def addUsertoRemoteDesktop(username):
    cmd = "net localgroup "+chr(34)+"Remote Desktop Users "+chr(34) + username +" /add"
    print(cmd)
    #os.system(cmd)
    return subprocess.run(shlex.split(cmd),capture_output=True)

def createProfile(username,ou1,ou2,domain,ipServer,nameFolder,password):
    cmdMkdir = "mkdir C:\\profiles\\"+nameFolder
    print(cmdMkdir)
    os.system(cmdMkdir)
    cmdshare = "net share "+nameFolder+"=C:\\profiles\\"+nameFolder +" /grant:everyone,full"
    print(cmdshare)
    os.system(cmdshare)
    pathProfile =" -profile "+ chr(92)+chr(92)+ipServer+"\\profiles\\"+username
    #print(pathProfile)
    # pathHomeDir = " -hmdir "+chr(92)+chr(92)+"192.168.10.133\\dungchung\\"+username+" -hmdrv Z:"
    command="dsmod user "+ chr(34)+"cn="+username+",ou="+ou1+","+"ou="+ou2+","+domain+chr(34)+ pathProfile
    print(command)
    os.system(command)

def installService():
    # cmd = " powershell.exe Install-WindowsFeature -name Web-Server -IncludeManagementTools"
    cmd = " powershell.exe Install-WindowsFeature -name telnet-client"
    print(cmd)
    os.system(cmd)
    cmd2 = "powershell.exe Install-WindowsFeature -Name Web-Ftp-Server -IncludeAllSubFeature -IncludeManagementTools -Verbose"
    print(cmd2)
    os.system(cmd2)

def removeService():
    # cmd1 = "Uninstall-WindowsFeature -Name Web-Server -ComputerName DC2022 -Credential demo\administrator 1"
    # cmd2 = "Uninstall-WindowsFeature -telnet-client -ComputerName DC2022 -Credential demo\administrator 1"
    cmd1 = "powershell.exe Import-Module ServerManager"
    print(cmd1)
    os.system(cmd1)
    cmd2 = "powershell.exe Remove-WindowsFeature telnet-client"
    print(cmd2)
    os.system(cmd2)
    cmd3 = "powershell.exe Remove-WindowsFeature Web-Server"
    print(cmd3)
    os.system(cmd3)

def splitName(ten):
    a = ten.strip().split(" ")
    kq = a[-1]
    for i in range(len(a)-1):
        kq = kq + a[i][0]
    return kq

def formatUsername(user):
    if user.find("ï»¿")!=-1:
        return user.replace("ï»¿","")
    else:
        return user

def readCSVFile(tenfile):
    csvFile= open(tenfile,"r")
    rowCSV = csv.reader(csvFile)
    for row in rowCSV:
        createUser(splitName(formatUsername(row[0])),row[2],row[1],"DATA","dc=hihi,dc=com")

def menu():
    while True:
        print(" ")
        print("Nhan 1 de tao user")
        print("Nhan 2 de doi mat khau user")
        print("Nhap 3 de tao profile cho user")
        print("Nhan 4 cai service")
        print("Nhan 5 de xoa user")
        print("Nhan 6 de tao user tu file csv")
        print("Nhan 7 remove Service")
        print("Nhan 8 de thiet lap user co quyen remote desktop")
        print("Nhan 9 de tao ouCha")
        print("Nhan 10 de tao ouCon")
        chon = int(input("Nhap lua chon cua ban: "))
        if chon ==1:
            username=splitName(input("Nhap ho va ten cua user: "))
            password = input("Nhap mat khau: ")
            ou = input("Nhap ou Con: ")
            ou1 = input("Nhap ou Cha:")
            createUser(username,password,ou,ou1,"dc=hihi,dc=com")
        elif chon ==2:
            username = input("Nhap username: ")
            newpassword = input("Nhap mat khau moi: ")
            ou1 = input("Nhap OU Con:")
            ou2= input("Nhap OU Cha:")
            domain ="dc=hihi,dc=com"
            changePass(splitName(username),newpassword,ou1,ou2,domain)
        elif chon==3:
            username = input("Nhap username: ")
            newpassword = input("Nhap mat khau moi: ")
            ou1 = input("Nhap OU Con: ")
            ou2 = input("Nhap OU Cha:")
            domain ="dc=hihi,dc=com"
            ipServer = input("Nhap IP cua Server: ")
            nameFolder = input("Nhap ten thu muc muon tao Profile: ")
            password = input("Nhap password: ")
            createProfile(splitName(username),ou1,ou2,domain,ipServer,nameFolder,password)
        elif chon == 4:
            installService()
        elif chon ==5:
            userdel = input("Nhap user muon xoa: ")
            ou2= input("Nhap OU Cha:")
            ou1=input("Nhap OU Con:")
            domain ="dc=hihi,dc=com"
            removeUser(splitName(userdel),ou1,ou2,domain)
        elif chon ==6:
            readCSVFile("DATASERVER.csv")
        elif chon ==7:
            removeService()
        elif chon == 8:
            username = input("Nhap ten username: ")
            addUsertoRemoteDesktop(splitName(username))
        elif chon == 9:
            ou= input("Nhap ou muon tao:")
            domain = "dc=hihi,dc=com"
            createOuParent(ou, domain)
        elif chon == 10:
            ou1= input("Nhap ou con muon tao:")
            ou2=input("Nhap ou cha:")
            domain = "dc=hihi,dc=com"
            createOuChild(ou1,ou2, domain)
                
        
if __name__ == '__main__':
    menu()
