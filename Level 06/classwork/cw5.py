#5) მოცემულია ორი რიცხვი a და b. თუ  ერთ-ერთი მაინც  მეტია 5-ზე, დაბეჭდე "ერთ-ერთი პირობა მაინც სწორია", წინააღმდეგ შემთხვევაში — "არც ერთი პირობა არ შესრულდა"
number1=int(input("enter your number"))
number2=int(input("enter your number"))

if number1>5 or number2 >5:
    print("ert-erti piroba mainc sworia")
else:
    print("arcerti piroba ar shesrulda")