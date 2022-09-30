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

    a =re.findall('.+@\.[a-z]',b)  # .+ accounts for one more character .* accounts for 0 or more characters
    if a!=[]:
        flag = 1

    if flag == 0:
        l = re.findall(".+@.+\.[a-z]",b)
        if l!=[]:
            #print("Your email id is valid\n")
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
                print("You have entered a invalid password\nEnter a Valid Password with min 5 & max 16 characters\nAnd your passowrd must have atleast 1 digit, 1 uppecase, 1 lowercase & 1 special character\n")
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
    b = input("Enter your username\n")
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
            print("Login Sucessfull")
            print("WELCOME")
            print("*************************************")
        else:
            print("*************************************")
            print("Incorrect Password\nPress 1 to retrieve your password\nPress 2 to Change Password\nPress 3 to Register has New User\nPress 4 to exit\n*************************************\n")
            p = input()
            if p == "1":
                b = input("Enter your valid Email id\n")
                if b in data:
                    print("Your Password is",data[b])
                else:
                    print("Invalid Username")
            elif  p == "2":
                b = input("Enter your valid Email id\n")
                print(data)
                if b in data:
                    db_w = open("temp.txt","w")
                    s1 = ' '
                    while s1:
                        s1 = db.readline()  #read the first line
                        l1 = s1.split("~~~")
                        print(s1)
                        print(l1)
                        if len(s1)>0:
                            if l1[0] == b:
                                newpass = input("Enter your new password")
                                db_w.write(b+", "+newpass+"\n")
                            else:
                                db_w.write(s1)
                    db_w.close()
                    db.close()
                    #os.remove("custdata.txt")
                    #os.rename("temp.txt","custdata.txt")
                else:
                    print("Invalid Username")
                    print("*******************************************\n")
            elif p == "3":
                registration()
            elif p == "4":
                exit()
            else:
                print("Invalid Key Pressed")
                print("*******************************************\n")


    else:
        print("Incorrect Username & Register again")
        print("*******************************************\n")

print("****** WELCOME TO GUVI NETWORK ******")
a = input("Enter your choice:\nPress 1 for LOGIN \nPress 2 for Registration\n")
print("*************************************")
if a == "1":
    login()
elif a == "2":
    registration()
else:
    print("Press the Valid Number")
    print("*******************************************\n")