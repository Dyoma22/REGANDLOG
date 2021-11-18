from Funktsioonid import *
users=["Demid"]
passwords=["12345"]

while True:
    print("Reg-1,Avt-2,Väljä-3")
    v=int(input())
    if v==1:
        print("Registreerimine")
        #
        #log=...
        #pas=...
        users.append(log)
        passwords.append(pas)
    elif v==2:
        print("Avtoriseerimine")
        #
    elif v==3:
        print("Väljä")
        break
        #valmis
    else:
        print("On vaja valida 1,2 või 3")
