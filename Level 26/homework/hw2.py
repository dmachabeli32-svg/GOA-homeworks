# 2) შექმენი ცარიელი სია. მომხმარებელს შეაყვანინე რიცხვები სანამ "stop"-ს არ დაბეჭდავს, ყოველი ახალი რიცხვი: თუ ნაკლებია 50-ზე → ჩასვი სიის დასაწყისში (insert), თუ მეტია ან ტოლია 50-ის → დაამატე ბოლოში (append), ბოლოს დაბეჭდე სია

numbers = []

while True:
    number = input("enter any number or stop:")

    if number == "stop":
        break
    else:
        num = int(number)
        if num < 50:
            numbers.insert(0,num)
        else:
            numbers.append(num)
print(numbers)