# 5) შექმენი ნებისმიერი list 5 ელემენტით, მომხმარებელს ჰკითხე: გინდა list-ის გასუფთავება? (yes/no), თუ პასუხი "yes"  გამოიყენე clear(), ბოლოს დაბეჭდე list

name = ["dachi", "nika", "gio", "luka","gela"]

answer = input("list-ის გასუფთავება? (yes/no): ")

if answer == "yes":
    print(name.clear())

print(name)