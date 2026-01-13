# 8) მომხმარებელს შეაყვანინე 5 რიცხვი while loopით, დაითვალე მათი საშუალო, თუ საშუალო > 50 დაბეჭდე "დიდი საშუალო" წინააღმდეგ შემთხვევაში "პატარა საშუალო"

count = 0
total = 0

while count< 5:
    num = int(input("enter number"))
    count += 1
    total += num
    
avarage= total / 5

if avarage > 50:
    print("დიდი საშუალო.", avarage)
else:
    print("პატარა საშუალო",avarage)