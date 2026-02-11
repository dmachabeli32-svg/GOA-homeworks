# 2) შექმენი ფუქნცია სახელად numbers რომელიც მიიღებს პარამეტრად რაღაც რიცხვს და დაპრინტავს ეს რიცხვი კენტია თუ ლუწი

def numbers(num):
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
print(numbers)