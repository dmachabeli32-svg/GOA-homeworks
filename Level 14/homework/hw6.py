# მომხმარებელს შემოატანინე რიცხვი, მანამ სანამ არ შემოიტანს  ტექტს - 'გამოთვალე საშუალო'. როგორც კი ამ ტექტს შემოიყვანს დაპრინტეთ ყველა შემოტანილი რიცხვის საერთო საშუალო არითმეტიკული.

i=0
count=0
while True:
    num=input("enter your number:")
    if num == "gamotvale sashualo":
        break
    if num.isdigit():
        i+=int(num)
        count=count+1
    else:
        print("sheiyvanet ricxvi an gamotvalet sashualo")


if count>0:
    everage=i/count
    print("sashualo aritmetikuli aris",everage)
else:
    print("sheiyvane ricxvi:")
 