# 1) შექმენით ფუნქცია. მომხმარებელს შემოატანინეთ ერთი მთელი რიცხვი n. დაბეჭდეთ თუ რამდენი ლუწი რიცხვია 1-დან n-მდე. გამოიძახეთ ფუნქცია

def fun():
    num = int(input("sheiyvane ricxvi:"))
    count = 0

    for i in range(1,num+1):
        if i % 2 == 0:
            count += 1
    return(count)
print(fun())

# def count_even_numbers():
#     n = int(input("შეიყვანეთ მთელი რიცხვი n: "))
#     count = 0
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             count += 1
#     print("ლუწი რიცხვების რაოდენობაა:", count)
# count_even_numbers()
