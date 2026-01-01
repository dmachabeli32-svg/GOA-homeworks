# 1) შექმენი ცარიელი სია.მომხმარებელმა შეიყვანოს რიცხვები მანამ, სანამ არ დაწერს "stop".დაამატე მხოლოდ დადებითი რიცხვები სიაში, უარყოფითი რიცხვები არ დაამატო, ბოლოს დაბეჭდე სია

numbers = []

while True:
    number = input("enter any number or stop: ")

    if number == "stop":
        break
    else:
        num = int(number)
        numbers. append(num)

print(numbers)