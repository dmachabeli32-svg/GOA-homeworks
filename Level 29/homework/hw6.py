# 6)მომხმარებელს შემოატანინე რაიმე სტრინგი,შენი დავალებაა დაითვალო თუ რამდენი ცალი ხმოვანი და რამდენი ცალი თანხმოვანი გვხვდება მის მიერ შემოყვანილ სტრინგში

name = input("enter word:")

count = 0 
count1 = 0

for i in name:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count+=1
    else:
        count1+=1
print(count)
print(count1)