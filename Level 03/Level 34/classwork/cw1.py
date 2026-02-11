def fun():
    count = 0
    total = 0
    name = "erti vardisferi vardi"
    for i in name:
        if i != " ":
            count += 1
        else:
            total = count
            count = 0
            if total > 0 and count > total:
                total = count
    if count > total:
        total = count
    print(total)
fun()

            
            


