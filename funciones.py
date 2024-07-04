 
def añadi_jugador(listaj_jugador, juego):
    juegos=["FIFA","FORNITE","VALORANT"]
    listauser=[]
    iduser=input("Ingrese su id:")
    listauser.append(iduser)
    nombre=input("Ingrese su nombre:")
    listauser.append(nombre)
    while True:
        try:
            juego=input("Ingrese su juego:").upper()
            if juego in juegos:
                puntaje=int(input("Ingrese su puntaje obtenido:"))
                mas=input("Quiere ingresar mas juego y puntaje? (si/no)").lower()
                if mas=="si":
                    listauser.append(juego)
                    listauser.append(puntaje)
                    continue
                elif mas=="no":
                    listauser.append(juego)
                    listauser.append(puntaje)
                    break
            elif juego not in juegos:
                print("error juego no esta para registrar")
                print(f"Que estan son {juegos}")
        except:
            print("error vuelve ingresar los datos de juego!!!")
    if puntaje<=10000:
        rango="principiante"
        listauser.append(rango)
    elif puntaje>100000:
        rango="avanzado"
        listauser.append(rango)
    elif puntaje>1000000:
        rango="experto"
        listauser.append(rango)
    else:
        print("rango error")
    listaj_jugador.append(listauser)
    return listaj_jugador, juego  

def listajugador(lista):
    titulo=["Id", "Jugador", "Nombre", "Valorant", "Fornite", "FIFA", "Tipo" ]
    print(titulo)
    print(lista)
def imprimir(lista):

    import csv
    with open("juadores", "w", newline="") as archivo:
        datos=csv.writer(archivo)
        datos.writerow(["Id", "Jugador", "Nombre", "Valorant", "Fornite", "FIFA", "Tipo" ])
        datos.writerows(lista)
        print("imprimir")