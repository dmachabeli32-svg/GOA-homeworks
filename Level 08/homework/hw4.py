# 4) მომხმარებელს შემოატანინე:
# --> ასაკი (age)
# --> სტუდენტია თუ არა (student) – შეიყვანოს "yes" ან "no"
# შემდეგ:
# თუ ასაკი ნაკლებია 12-ზე ან მეტია 65-ზე -> "ბილეთი უფასოა"
# თუ student == "yes" და ასაკი მეტია 12-ზე -> "ბილეთი ნახევარ ფასად"
# სხვა შემთხვევაში -> "სრული ფასი უნდა გადაიხადო"

age=int(input("enter your age:"))
student=input("studentia?:")


if age < 12 or age > 65:
    print("bileti ufasoa")
elif student == "yes" and age > 12:
    print("bileti naxevar fasad")
else:
    print("sruli fasi unda gadaixado")