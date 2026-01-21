# 4)შექმენი სია და შეიყვანე სტრიგნები პატარა ასოებით,შენი დავალებაა შეამოწმო,თუ სტრინგი შეიცავს 5 ასოზე მეტს მაშინ ასეთი სიტყვები ჩაამატე ახალ სიაში ოღონდ პირველი ასო ქონდეთ დიდი ,ხოლო თუ სიტყვა შეიცავს 5 ასოზე ნაკლებს მაშინ დაამატე ეს ელემენტებიც სიაში ოღონდ ყველა ასო ქონდეთ დიდი

animals = ["dog", "monkey", "donkey", "pig", "horse"]

animals1 = []
i = 0 

while i < 5:
    if len(animals[i]) >= 5:
        animals1.append(animals[i].capitalize())
    else:
        animals1.append(animals[i].upper())
    i+=1
print(animals1)
