# მომხმარებელს შემოატანინეთ რიცხვი, ამ რიცხვის ჩათვლით შეკრიბეთ ყველა რიცხვი და გამოიტანეთ საბოლოო პასუხი.

n=int(input("enter your number:"))
count=0
for i in range(1,n+1):
    count+=i

print(count)