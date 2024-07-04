import funciones as fn
op=0
rango_jgador={
    "principante": [],
    "avanzado" : [],
    "experto" : []
}
jugadores=[]
while True:
    try:
        print("******eShirlitos******")
        print("1.\tRegistrar puntajes torneo")
        print("2.\tListar los puntajes")
        print("3.\tImprimir por Tipo")
        print("4.\tSalir")
        op=int(input("Ingresa opcion:"))
        if op==1:
            print("pase")
            juego=[]
            fn.añadi_jugador(jugadores,juego)
            for fila in range(len(jugadores)):
                print(jugadores[fila][4])  
        elif op==2:
            print("pase")
            fn.listajugador(jugadores)
        elif op==3:
            print("pase")
            fn.imprimir(jugadores)
        elif op==4:
            print("pase")
            break
    except:
        print("error")
    