
# შექმენი ცვლადი და შეინახე შენი პაროლი(string)
# მომხმარებელს შემოატანინე პაროლი
# სანამ შენი პაროლი არ უდრის მომხმარებლის მიერ შემოტანილ პაროლს
#     მომხმარებელს თავიდან შემოატანინე პაროლი რომ გაარტყას შენ პაროლს
# დაპრინტე "სწორია გაარტყი"
# -> გადააკეთეთ ზემოთ მოცემული ტექსტი კოდად(ინდენტაცია დაცულია


user_password = input("enter your password:")

i = 0

while user_password != "0000":
    print("password is incorrect")
    user_password = input("enter your password: ")

i=i+1

print("correct")