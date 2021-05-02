import random
print("hey human lets play, rock , paper, scissors")
print("no of chances - 5")
ip=["r","p","s"]
mscore=0
hscore=0
for i in range(5):
    c_ip= random.choice(ip)
    u_ip= input("enter r or s or p")
    print(f'machines input id : {c_ip}')
    print(f"your input id : {u_ip}")
    if c_ip==u_ip:
        print("tie")
    elif (
            (c_ip=="r"and u_ip=="s")or
            (c_ip=="s"and u_ip=="p")or
            (c_ip=="p"and u_ip=="r")
    ):
        print("##### machine wins ######")
        mscore=+1
    else:
        print("$$$$$ you wins $$$$$")
        hscore+=1
print("---------------------------------------")
if(hscore>mscore):
    print(f"your score : {hscore} and machine score : {mscore}")
    print("you wins....")
elif (hscore== mscore):
    print(f"your score : {hscore} and machine score : {mscore}")
    print("tie")
else:
    print(f"your score : {hscore} and machine score : {mscore}")
    print("machine wins")
