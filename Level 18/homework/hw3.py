# 3)
# მომხმარებელს შემოაყვანინე  რიცხვი.

# თუ რიცხვი დადებითია, შიგნით შეამოწმე:

#     თუ ლუწია, დაბეჭდე "დადებითი ლუწი".

#     თუ არა — "დადებითი კენტი".

# სხვა შემთხვევაში დაბეჭდე --> "რიცხვი უარყოფითია"

num=int(input("enter your number:"))
if num > 0:
    if num % 2== 0:
        print("dadebiti luwi")
    else:
        print("uaryofiti luwi")
else:
    print("ricxvi uaryofitia")