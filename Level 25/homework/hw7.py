# 7) შექმენი list: letters = ["a", "b", "c", "d", "e"] მომხმარებელს შეაყვანინე ინდექსი, pop()-ით წაშალე ამ ინდექსზე მდგომი ელემენტი, დაბეჭდე წაშლილი ელემენტი და list

letters = ["a", "b", "c", "d", "e"]

num = int(input("enter index:"))

removed = letters.pop(num)

print(letters,removed)