# 1)შექმენი სია სადაც მოათავსებთ განსხვავებული ტიპის მონაცემებს,შენი დავალებაა რომ გაიგო თუ რამდენი ცალი სტრინგ ტიპის მონაცემი გვხვდება სია

data = ["apple", 10, 5.14, "banana", True, "orange", None]

count = 0

for i in data:
    if type(i) == str:
        count += 1
    
print(count)


