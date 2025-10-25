# #1) მომხმარებელს შემოატანინე ტემპერატურა (რიცხვი) და შემდეგ შეამოწმე:
# თუ ტემპერატურა მეტია 30-ზე -> დაბეჭდე "ძალიან ცხელა!"
# თუ ტემპერატურა მეტია 20-ზე -> დაბეჭდე "სასიამოვნო ამინდია"
# თუ ტემპერატურა მეტია 10-ზე -> დაბეჭდე "ცოტა ცივა"
# თუ ტემპერატურა მეტია 0-ზე -> დაბეჭდე "ცივა, ჩაიცვი თბილად"
# სხვა შემთხვევაში -> "გაიყინები, სახლში დარჩი!"

temp=int(input("enter your tempeerature"))

if temp > 30:
    print("dzalian cxela")
elif temp > 20:
    print("sasiamovno amindia")    
elif temp > 10:
    print("cota civa")
elif temp > 0:
    print("civa chaicvi tbilad")
else:
    print("gaiyinebi darchi saxshi")