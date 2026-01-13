# 7) მომხმარებელს შეაყვანინე რიცხვი 1–5. დაბეჭდე სიტყვებით, მაგალითად: 1 → One 2 → Two გამოიყენე if / elif / else

name = int(input("enter number from 1 to 5:"))


if name == 1:
    print("one")
elif name == 2:
    print("two")
elif name == 3:
    print("three")
elif name == 4:
    print("four")
elif name == 5:
    print("five")
else:
    name = int(input("enter number from 1 to 5:"))