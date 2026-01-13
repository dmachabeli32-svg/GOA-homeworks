# 1) მომხმარებელს შემოაყვანინე წინადადება. დაბეჭდე თითოეული სიტყვა ცალ–ცალკე for loop-ის გამოყენებით. თითოეული სიტყვა დაბეჭდე capitalize()-ით.

name = input("enter sentence:")

for i in name.split():
    print(i.capitalize())

