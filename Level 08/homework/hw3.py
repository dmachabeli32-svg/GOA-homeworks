# 3) მომხმარებელს შემოატანინე:
# --> ტემპერატურა (temp)
# --> არის თუ არა წვიმა (rain) – მომხმარებელმა შეიყვანოს "yes" ან "no"
# შემდეგ შეამოწმე:
# თუ ტემპერატურა მეტია 25-ზე და rain == "no" -> "შესანიშნავი ამინდია სასეირნოდ!"
# თუ ტემპერატურა მეტია 25-ზე და rain == "yes" -> "ცხელი და წვიმიანია, ჩაფხუტი დაგჭირდება!"
# თუ ტემპერატურა ნაკლებია 10-ზე ან rain == "yes" -> "სჯობს სახლში დარჩე"
# სხვა შემთხვევაში -> "სასიამოვნო ამინდია"

temp=int(input("enter temperature:"))
rain=input("is it rain?:")

if temp > 25 and rain == "no":
    print("shesanishnavi amindia saseirnod")
elif temp > 25 and rain == "yes":
    print("cxeli da wvimiania, chafxuti dagwirdeba! ")
elif temp < 10 or rain == "yes":
    print("jobia saxshi darche")
else:
    print("sasiamovno amindia")