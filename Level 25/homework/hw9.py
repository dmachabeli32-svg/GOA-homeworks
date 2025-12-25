# 9) შექმენი list: nums = [1, 2, 3, 4] მომხმარებელს შეაყვანინე: ინდექსი და რიცხვი, თუ ინდექსი list-ის საზღვრებშია გამოიყენე insert() ჩასამატებლად, თუ ინდექსი ლისტზე დიდია მაშინ გამოიყენე append()

nums = [1, 2, 3, 4]

num = int(input("enter your number:"))
index = int(input("enter your index:"))

if 0 <= index < len(nums):
    nums.insert(index, num)  
    print("რიცხვი დაემატა ინდექსზე {index}.")
else:
    nums.append(num)  
    print("რიცხვი დაემატა სიაში ბოლოს.")

print("განახლებული ჩამონათვალი:", nums)