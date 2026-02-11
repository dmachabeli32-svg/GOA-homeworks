# 7) შექმენი ფუქნცია რომელიც მომხმარებელს შემოაყვანინებს რაღაც რიცხვს და დააბრუნებს სიტყვას ეს რიცხვი დადებითია უარყოფითია თუ ნულია
def number_check():
    number = int(input("shemoagde ricxvi dzma: "))

    if number > 0:
        return "iasnad rom dadebitia"
    elif number < 0:
        return "iasnad rom uaryofitia"
    else:
        return "arafers warmoadgens"
    
print(number_check())
    
