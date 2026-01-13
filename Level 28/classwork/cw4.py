# 4) მომხმარებელს შემოაყვანინე ასაკი, თუ ასაკინ < 18-ზე -> "შენ ხარ არასრულწლოვანი", თუ ასაკი 18 და 64 შორისაა -> "შენ ხარ სრულწლოვანი", თუ ასაკი > 65-ზე -> "შენ ხარ პენსიონერი"

age = int(input("enter your age"))

if age < 18:
    print("arasrulwovani xar")
elif age >18 and age <64:
    print("srulwlovani xar")
else:
    print("pensioneri xar")







