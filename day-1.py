with open("day1.txt", "r") as f:
    ordenes = [
        linea.strip() for linea in f if linea.strip() and linea.strip()[0] in ["R", "L"]
    ]

point = 50
ceros = 0
for orden in ordenes:
    letra = orden[0]
    numero = int(orden[1:])
    point = (point + (numero if letra == "R" else -numero)) % 100
    if point == 0:
        ceros += 1

print(point, ceros)
