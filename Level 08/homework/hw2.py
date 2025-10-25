# 2) მომხმარებელს შემოატანინე ორი რიცხვი:
# --> ქულა (score)
# --> დასწრება (attendance პროცენტებში)
# შემდეგ შეამოწმე:
# თუ ქულა მეტია 80-ზე და დასწრება მეტია 90-ზე -> "შენ შესანიშნავად დაწერე გამოცდა"
# თუ ქულა მეტია 50-ზე და დასწრება მეტია 70-ზე -> "საშუალოდ დაწერე გამოცდა"
# თუ ქულა მეტია 30-ზე ან დასწრება მეტია 50-ზე -> "გაჭირვებით, მაგრამ ჩააბარე გამოცდა"
# ყველა სხვა შემთხვევაში → "ჩაიჭერი!"

score=int(input("enter your score:"))
att=int(input("enter your attendance"))

if score > 80 and att > 90:
    print("shen shesanishavad dawere gamocda")
elif score > 50 and att > 70:
    print("sashualod dawere gamocda")
elif score > 30 and att >50:
    print("gawirvebit magram chaabare gamocda")
else: 
    print("chaiweri")