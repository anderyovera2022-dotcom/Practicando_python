rating= float(input("Ingrese las estrellas: "))
if rating >= 4.5:
    print("Extraordinario")
elif rating >= 4 and rating < 4.5:
    print("Exelente")
elif rating >= 3 and rating < 4:
    print("Bueno")
elif rating >= 2 and rating < 3:
    print("Fair")
else:
    print("Poor")
