import re
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
            print("Your email id is valid\n")
            pwd = input("Enter your password\n")
            m =[]
            n = []
            for k in db:
                x,y = k.split(", ")
                y = y.strip()
                m.append(x)
                n.append(y)
            data = dict(zip(m,n))
            if len(pwd) <= 6:
                print("Password too short or too long")
                registration()
            elif b in m:
                print("Email Already exist Try Different Email id")
                registration()
            else:
                db = open("custdata.txt","a")
                db.write(b+", "+pwd+"\n")
                print("Your Email & Password is Saved")
    else:
        print("Enter the correct email id")

def login():
    db = open("custdata.txt", "r")
    b = input("Enter your username\n")
    pwd = input("Enter your password\n")
    m = []
    n = []
    for k in db:
        x, y = k.split(", ")
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
            print("Incorrect Password - Press 1 to retrieve your password")
            p = input()
            if p == "1":
                b = input("Enter your valid Email id\n")
                if b in data:
                    print("Your Password is",data[b])
                else:
                    print("Invalid Username")
            else:
                print("Invalid Key Pressed")


    else:
        print("Incorrect Username or Register again")



print("****** WELCOME TO GUVI NETWORK ******")
a = input("Enter your choice:\nPress 1 for LOGIN \nPress 2 for Registration\n")
print("*************************************")
if a == "1":
    login()
elif a == "2":
    registration()
else:
    print("Press the Valid Number")