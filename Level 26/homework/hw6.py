# 6) მომხმარებელს შემოაყვანინე რიცხვები, შექმენი ორი სია დადებითი და უარყოფითი სიებისთვის, დადებითი რიცხვები დაამატე დადებითი რიცხვებისთვის განკუთვნილ სიაში, უარყოფითი რიცხვები კი პირიქით


positive = []
negative = []

while True:
    number = input("enter any number or stop:")

    if number == "stop":
        break
    num = int(number)
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)

print(positive, negative)
