# 3) შექმენი ცარიელი სია. მომხმარებელს შემოაყვანინე რიცხვები, ყოველი რიცხვი დაამატე სიაში,როცა სიაში მყოფი რიცხვების ჯამი გახდება 100-ზე მეტი, შეწყვიტე რიცხვების შეყვანა, ბოლოს დაბეჭდე სია და მათი ჯამი

numbers = []

while True:
    number = int(input("enter numbers:"))
    numbers.append(number)
    result = sum(numbers)
    if  result > 100:
        break

print(numbers, result)
    
