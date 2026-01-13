# 6) მომხმარებელს შეაყვანინე ასაკი მანამ, სანამ არ შეიყვანს -1. დაბეჭდე რამდენი ადამიანი იყო არასრულწლოვანი, სრულწლოვანი, პენსიონერი. გამოიყენე while loop + if/elif/else


count = 0
count2 = 0
count3 = 0

while True:
    age = int(input("enter age:"))
    if age == -1:
        break
    elif age <18:
        count += 1
        print("არასრულწლოვანი")
    elif age >=18 and age <60:
        count2 += 1
        print("სრულწლოვანი")
    else:
        count3 += 1
        print("პენსიონერი")

if count >=1:
    print(" არასრულწლოვანი იყო", count)
if count2 >=1:
    print("სრულწლოვანი იყო", count2)
if count3 >=1:
    print("პენსიონერი იყო", count3)