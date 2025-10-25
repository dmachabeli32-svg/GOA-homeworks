# 5) მომხმარებელს შემოატანინე:
# --> მომხმარებლის სახელი (username)
# --> პაროლი (password)
# შეამოწმე:
# თუ მომხმარებელი არის "admin" და პაროლი არის 'superSecretPassword' → "მოგესალმები, ადმინ!"
# თუ მომხმარებელი "guest" და პაროლი არის "1234" → "მოგესალმები, სტუმარო!"
# სხვა შემთხვევაში → "მომხმარებელი არ მოიძებნა!"


user=input("enter your username:")
password=input("enter your password")

if user == "admin" and password == "superSecretPassword":
    print("mogesalmebit admin")
elif user == "guest" and password == "1234":
    print(" mogesalmebi, stumaro")
else: 
    print("momxmarebeli ar moidzebna")