# 2) შექმენით ფუნქცია. შექმენით რიცხვებით სავსე სია, დაბეჭდეთ სიის უდიდესი ელემენტი. არ გამოიყენოთ max() ფუნქცია, გამოიყენეთ for ციკლი. გამოიძახეთ ფუნქცია.
def numbers():
    sia = [1, 2, 3, 4, 5, 6, 7, 9]
    biggest = sia[0]

    for i in sia:
        if i > biggest:
            biggest = i
    print(biggest)
numbers()