# 5) მომხმარებელს შემოაყვანინე რიცხვები, ეს რიცხვები დაამატე სიაში და გამოითვალე ამ რიცხვების საშუალო არითმეტიკული.

numbers = []

while True:
    number = input("enter any number or stop: ")

    if number == "stop":
        break
    else:
        num = int(number)
        numbers. append(num)

name = sum(numbers) / len(numbers)
print(numbers, name)