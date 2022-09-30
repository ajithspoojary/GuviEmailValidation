import re
import os
def registration():
    db = open("custdata.txt","r")
    sc = '!@#$%^&*(){}|:"<>?_+/*-1234567890=[]\;,./~`'
    b = input("Enter the valid Email ID\n")
    flag = 0
    for i in sc:
        if i == b[0]:
            flag = 1
    d = re.findall("^/d",b)
    if d!=[]:
        flag = 1

    a =re.findall('.+@\.[a-z]',b)
    if a!=[]:
        flag = 1
    if flag == 0:
        l = re.findall(".+@.+\.[a-z]",b)
        if l!=[]:
            m =[]
            n = []
            for k in db:
                x,y = k.split("~~~")
                y = y.strip()
                m.append(x)
                n.append(y)
            data = dict(zip(m,n))
            if b in m:
                print("Email Already exist Try Different Email id")
                registration()
            pwd = input("Enter your password\n")
            check = True
            while check:
                if (len(pwd) < 5 or len(pwd) > 16):
                    break
                elif not re.search("[a-z]",pwd):
                    break
                elif not re.search("[0-9]",pwd):
                    break
                elif not re.search("[A-Z]",pwd):
                    break
                elif not re.search("[@#$%^&*_+-]",pwd):
                    break
                elif re.search("\s",pwd):
                    break
                else:
                    print("Your Password is Valid")
                    check = False
                    break

            if check:
                print("************************************************************************")
                print("YOU HAVE ENTERED A INVALID PASSWORD\nEnter a Valid Password with more than 5 & less than 16 characters\nAnd your passowrd must have atleast 1 digit, 1 uppecase, 1 lowercase & 1 special character")
                print("************************************************************************")

            else:
                db = open("custdata.txt","a")
                db.write(b+"~~~"+pwd+"\n")
                print("Your Email & Password is Saved")
                print("*******************************************")
    else:
        print("Enter the correct email id")

def login():
    db = open("custdata.txt","r")
    print("*******************************************")
    b = input("Enter your email\n")
    pwd = input("Enter your password\n")
    m = []
    n = []
    for k in db:
        x, y = k.split("~~~")
        y = y.strip()
        m.append(x)
        n.append(y)
    data = dict(zip(m, n))
    if b in data:
        if pwd == data[b]:
            print("*************************************")
            print("Login Successfull")
            print("WELCOME TO GUVI NETWORK")
            print("*************************************")
        else:
            print("*************************************")
            print("XXXXX    INCORRECT PASSWORD    XXXXX\n\nForgot Password !!! Then\nPress 1 to Retrieve your password\nPress 2 to Change Password\nPress 3 to Register has New User\nPress 4 to Exit\n*************************************\n")
            p = input()
            if p == "1":
                b = input("Enter your valid Email id\n")
                if b in data:
                    print("Your Password is",data[b])
                else:
                    print("Invalid Email")
            elif  p == "2":
                b = input("Enter your valid Email id\n")
                if b in data:
                    db = open("custdata.txt", "r")
                    db_w = open("temp.txt", "w")
                    s1 = ' '
                    while (s1):
                        s1 = db.readline()
                        l1 = s1.split("~~~")
                        if len(s1) > 0:
                            if l1[0] == b:
                                newpass = input("Enter your new password\n")
                                check = True
                                while check:
                                    if (len(newpass) < 5 or len(newpass) > 16):
                                        break
                                    elif not re.search("[a-z]", newpass):
                                        break
                                    elif not re.search("[0-9]", newpass):
                                        break
                                    elif not re.search("[A-Z]", newpass):
                                        break
                                    elif not re.search("[@#$%^&*_+-]", newpass):
                                        break
                                    elif re.search("\s", newpass):
                                        break
                                    else:
                                        print("Your Password is Updated")
                                        check = False
                                        break

                                if check:
                                    print("************************************************************************")
                                    print("XXXXXXXX YOU HAVE ENTERED INVALID PASSWORD XXXXXXXX\n1. Enter a Valid Password with more than 5 & less than 16 characters\n2. And your passowrd must have atleast 1 digit, 1 uppecase, 1 lowercase & 1 special character")
                                    print("************************************************************************")
                                    db_w.write(b + "~~~" + data[b] + "\n")
                                else:
                                    db_w.write(b + "~~~" + newpass + "\n")
                            else:
                                db_w.write(s1)
                    db_w.close()
                    db.close()
                    os.remove("custdata.txt")
                    os.rename("temp.txt", "custdata.txt")
                else:
                    print("Invalid Email")
                    print("*******************************************\n")
            elif p == "3":
                registration()
            elif p == "4":
                exit()
            else:
                print("Invalid Key Pressed")
                print("*******************************************\n")


    else:
        print("*******************************************")
        print("Incorrect Email - Register again")
        print("*******************************************\n")

print("****** WELCOME TO GUVI NETWORK ******")
a = input("ENTER YOUR CHOICE:\nPress 1 for LOGIN \nPress 2 for REGISTRATION\n*************************************\n\n")
if a == "1":
    login()
elif a == "2":
    registration()
else:
    print("Press the Valid Choice")
    print("*******************************************\n")