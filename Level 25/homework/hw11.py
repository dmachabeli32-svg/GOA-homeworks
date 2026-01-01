# 11) შექმენი ცარიელი list მომხმარებელს შემოაყვანინე რიცხვები მანამ სანამ არ დაწერს "stop", ყველა რიცხვი დაამატე ლისთში append()ის გამოყენებით და საბოლოოდ დაბეჭდე ლისთი


numbers = []

while True:
    user_input = input("შეიყვანეთ რიცხვი ან დაწერეთ 'stop', რომ შეწყვიტოთ: ")
    
    if user_input == "stop":
        break  
    else:
        if user_input.isdigit():  
            number = int(user_input)
            numbers.append(number) 
        else:
            print("გთხოვთ, შეიყვანოთ valido რიცხვი ან 'stop'.")

print("შეკრებული რიცხვები:", numbers)