import math
import random
dimensiones = (9, 9)

def dar_juego_por_filas(cadena:str):
    tamanio = len(cadena)
    raiz = int(math.sqrt(tamanio))
    filas,columnas = raiz,raiz
    k = 0
    juego = ""
    for i in range(filas):
        linea = ""
        for j in range(columnas):
            linea += cadena[k]
            k += 1
        juego += linea + "\n"
    return juego

def convertir_a_matriz(juego:str,dimensiones:tuple)->list:
    matriz = []
    alto = dimensiones[0]
    ancho = dimensiones[1]
    contador = 0
    for i in range(alto):
        fila = []
        for l in range(ancho):
            fila.append(int(juego[contador]))
            contador += 1
        matriz.append(fila)

    return matriz

def imprimir_tablero(matriz:list,dimensiones:tuple)->None:

    tablero = ""
    contador_raya = 0
    contador_espacio = 0
    contador_filas = 0

    for l in matriz:
        fila = l
        for t in fila:
            contador_raya += 1
            contador_espacio += 1
            tablero += str(t)+" "
            if contador_raya == 3:
                tablero += "|"
                contador_raya = 0
            if contador_espacio == 9:
                tablero += "\n"
                contador_espacio = 0
                contador_filas += 1
            if contador_filas == 3:
                tablero += "------+-------+------\n"
                contador_filas = 0
    
    tablero = "\n"+str(tablero[0:-23])+"\n"

    return tablero

def dar_diccionario_juegos()->dict:
    dificultades = ["faciles","intermedios","dificiles"]
    juegos_por_dificultad = {}

    for d in dificultades:
        archivo = open(d+".txt","r")
        linea = archivo.readline().replace("\n", "")
        juegos_por_dificultad[d]=[]
        while len(linea) > 0:
            lista = juegos_por_dificultad[d]
            lista = lista.append(linea)
            linea = archivo.readline().replace("\n", "")
        archivo.close()

    return juegos_por_dificultad

def dar_juego_aleatorio_por_dificultad(dificultad:str)->str:

    diccionario = dar_diccionario_juegos()
    lista_dificultad = diccionario[dificultad]
    cadena = lista_dificultad[random.randint(0,len(lista_dificultad))]
    sudoku = imprimir_tablero(convertir_a_matriz(cadena,(9,9)), (9,9))

    return sudoku

def verificar_filas(matriz: list) -> bool:

    correcto = True

    for i in matriz:
        fila = i
        numeros = []
        if 0 in fila:
            correcto = False
        else:
            for l in fila:
                if l not in numeros:
                    numeros.append(l)
                else:
                    correcto = False

    return correcto

def verificar_columnas(matriz:list)->bool:

    correcto  = True
    numeros = []

    for i in matriz:
        fila = i
        for l in fila:
            numero = l
            if numero == 0:
                correcto = False
                break
            else:
                if numero not in numeros:
                    numeros.append(numero)
                else:
                    correcto == False
                    break 
        numeros = []
    
    return correcto

def verificar_regiones(matriz:list)->bool:

    correcto  = True
    numeros = []
    repeticiones = 1
    cortes = [(0, 3), (3, 6), (6, 10)]
    
    while repeticiones <= 3:
        for i in matriz:
            fila = i
            for l in cortes:
                corte = l
                corte_inicial = corte[0]
                corte_final = corte[1]
                corte = fila[corte_inicial:corte_final]
                for t in corte:
                    numero = t
                    if numero == 0:
                        correcto = False
                        break
                    else:
                        if numero not in numeros:
                            numeros.append(numero)
                        else:
                            correcto = False
                            break
            numeros = []
        repeticiones += 1    

    return correcto

def verificar_juego(matriz:list)->bool:
    return verificar_filas(matriz) and verificar_columnas(matriz) and verificar_regiones(matriz)

def console():
    file_route = input("Type the file name you want: ")
    file = open(file_route)
    string = file.readline()
    complete_string = ""
    while string != "":
        complete_string += string.replace("\n", "")
        string = file.readline()
        
    print(dar_juego_por_filas(complete_string))

print(console())