# username: python     pass: rules

crd1 = input("username: ")
crd2 = input("password: ")

while crd1 != "python" or crd2 != "rules":
    if crd1 != "python":
        print("invalid username!\nPääsy evätty.")
        crd1 = input("username: ")
        crd2 = input("password: ")
    elif crd2 != "rules":
        print("invalid password!\nPääsy evätty.")
        crd1 = input("username: ")
        crd2 = input("password: ")
else:
    if crd1 == "python" and crd2 == "rules":
        print("Tervetuloa!")
