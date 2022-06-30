import os

os.system("cls")
lista_youtube1=["https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=QkGnxssjZEo",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=eCs8LT290a4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=M5QY2_8704o",
                "https://www.youtube.com/watch?v=xsVys0OMiYQ",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=QkGnxssjZEo",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=eCs8LT290a4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=M5QY2_8704o",
                "https://www.youtube.com/watch?v=xsVys0OMiYQ",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=QkGnxssjZEo",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=eCs8LT290a4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=M5QY2_8704o",
                "https://www.youtube.com/watch?v=xsVys0OMiYQ",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=QkGnxssjZEo",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=eCs8LT290a4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=M5QY2_8704o",
                "https://www.youtube.com/watch?v=xsVys0OMiYQ",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=QkGnxssjZEo",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=eCs8LT290a4",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=M5QY2_8704o",
                "https://www.youtube.com/watch?v=xsVys0OMiYQ",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=QkGnxssjZEo",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=PJxxfilLnGI",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=IWcswwIGejg",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=LOYYteCRks8",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
                "https://www.youtube.com/watch?v=M5QY2_8704o",
                "https://www.youtube.com/watch?v=xsVys0OMiYQ",
                "https://www.youtube.com/watch?v=ewSwphkNBi4",
]
lista_youtube2=[]

print("Longitud si filtrar:", len(lista_youtube1))
for item in lista_youtube1:
    if item not in lista_youtube2:
        lista_youtube2.append(item)
longitud = len(lista_youtube2)

print("Longitud filtrada:", longitud)

def ejecutar(argumento):
    #El argumento es el link que vamos a pasar
    print("Link real => ", argumento)

for i in range(longitud):
    ejecutar(lista_youtube2[i])