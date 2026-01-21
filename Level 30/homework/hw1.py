# 1) შექმენით სახელებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა და პირველი ასო არის d, მაშინ ახალ სიაში ჩაამატეთ სახელი "NIKA", თუ სიტყვის ყველა ასო არის დიდი ან იწყება ასო K-თი, მაშინ სიაში ჩაამატეთ სახელი "GOGA", სხვა შემთხვევაში სიაში ჩაამატეთ სიტყვა "ლიდერი". დაპრინტეთ მიღებული სია.


names = ["dachi", "keti", "dato", "nodari", "GIA"]
name = []


for i in names:
    if i == i.lower() and i[0] =="d": 
        name.append("NIKA")
    elif i == i.upper() or i[0] == "k":
        name.append("GOGA")
    else:
        name.append("leader")
print(name)