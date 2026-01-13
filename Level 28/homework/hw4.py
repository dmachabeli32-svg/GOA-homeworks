# 4) მომხმარებელს შემოაყვანინე 5 რიცხვი, დაბეჭდე მათი ჯამი. გამოიყენე for loop და while loop.


total = 0

for i in range(5):
    num = int(input("შეიყვანეთ რიცხვი: "))
    total += num

print(total)



total = 0
count = 0


while count < 5:
    num = int(input("შეიყვანეთ რიცხვი: "))
    total += num
    count += 1

print(total)
