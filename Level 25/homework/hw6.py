# 6) შექმენი ცარიელი list, მომხმარებელს 5-ჯერ შეაყვანინე რიცხვი, ყველა დაამატე list-ში და საბოლოოდ for loop-ის გამოყენებით დააჯამე რიცხვები რომელიც გექნება ლისტში

sia = []
amount = 0
num1 = int(input("enter number:"))
num2 = int(input("enter number:"))
num3 = int(input("enter number:"))
num4 = int(input("enter number:"))
num5 = int(input("enter number:"))

sia.append(num1)
sia.append(num2)
sia.append(num3)
sia.append(num4)
sia.append(num5)

for i in range(0 , 5):
    sia[0] += sia[i]

print(sia[0])
for i in range(0 , 5):
    amount += sia [i]
print (amount)