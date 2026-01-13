# 5) მომხმარებელს შეაყვანინე რიცხვები, მანამ სანამ არ შეიყვანს 0, ყოველი რიცხვის შემდეგ დაბეჭდე "დადებითია" ან "უარყოფითია".დაბეჭდე ბოლოს რიცხვების ჯამი. გამოიყენე while loop.

total = 0

while True:
    num = int(input("enter numbers or enter 0 to stop:"))
    total += num
    if num == 0:
        break
    elif num > 0:
        print("dadebitia")
    else:
        print("uaryofitia")

print(total)