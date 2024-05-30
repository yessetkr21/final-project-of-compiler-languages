def leer_lagramatica(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()

    num_casos = int(lineas[0].strip())
    gramatica = []
    indice = 1

    for _ in range(num_casos):
        num_no_terminales = int(lineas[indice].strip())
        indice += 1
        producciones = {}
        for _ in range(num_no_terminales):
            linea = lineas[indice].strip()
            no_terminal, reglas = linea.split(' -> ')
            producciones[no_terminal] = reglas.split('|')
            indice += 1
        gramatica.append(producciones)

    return gramatica
def calcular_primero(no_terminal, producciones, primero):
    if no_terminal in primero:
        return primero[no_terminal]

    primero[no_terminal] = set()
    for produccion in producciones[no_terminal]:
        if produccion == 'epsilon':  # Si la producción es epsilon agrega al conjunto "Primero".
            primero[no_terminal].add('epsilon')
        else:
            for simbolo in produccion:
                if simbolo.islower() or not simbolo.isalpha():
                    primero[no_terminal].add(simbolo)
                    break
                else:
                    simbolos_primero = calcular_primero(simbolo, producciones, primero)
                    primero[no_terminal].update(simbolos_primero - {'epsilon'})
                    if 'epsilon' not in simbolos_primero:
                        break
            else:
                primero[no_terminal].add('epsilon')

    return primero[no_terminal]


def calcular_todos_los_primeros(producciones):
    primero = {}
    for no_terminal in producciones:
        calcular_primero(no_terminal, producciones, primero)
    return primero


def calcular_siguiente(no_terminal, producciones, primero, siguiente, simbolo_inicial):
    if no_terminal in siguiente:
        return siguiente[no_terminal]

    siguiente[no_terminal] = set()
    if no_terminal == simbolo_inicial:
        siguiente[no_terminal].add('$') #todos los simbolos iniciales se les agrega dolar

    for nt in producciones:
        for produccion in producciones[nt]:
            for i, simbolo in enumerate(produccion):
                if simbolo == no_terminal:
                    if i + 1 < len(produccion):
                        siguiente_simbolo = produccion[i + 1]
                        if siguiente_simbolo.islower() or not siguiente_simbolo.isalpha():
                            siguiente[no_terminal].add(siguiente_simbolo)
                        else:
                            siguientes_primero = primero[siguiente_simbolo]
                            siguiente[no_terminal].update(siguientes_primero - {'epsilon'}) #Si es un no terminal, se agregan los símbolos del conjunto "Primero" del siguiente no terminal (excepto epsilon).
                            if 'epsilon' in siguientes_primero:
                                siguientes_siguiente = calcular_siguiente(nt, producciones, primero, siguiente, simbolo_inicial)
                                siguiente[no_terminal].update(siguientes_siguiente)
                    else:
                        if nt != no_terminal:
                            siguientes_siguiente = calcular_siguiente(nt, producciones, primero, siguiente, simbolo_inicial)
                            siguiente[no_terminal].update(siguientes_siguiente)

    return siguiente[no_terminal]

def calcular_todos_los_siguientes(producciones, primero, simbolo_inicial):
    siguiente = {}
    for no_terminal in producciones:
        calcular_siguiente(no_terminal, producciones, primero, siguiente, simbolo_inicial)
    return siguiente


def escribir_resultados(archivo_salida, gramatica, resultados_primero, resultados_siguiente):
    with open(archivo_salida, 'w') as f: #se crea la estructura n noterminals,nproducciones
        f.write(f"{len(gramatica)}\n")
        for i, producciones in enumerate(gramatica):
            f.write(f"{len(producciones)}\n")
            for nt in producciones:
                f.write(f"Pr({nt}) = {{{', '.join(sorted(resultados_primero[i][nt]))}}}\n")
            for nt in producciones:
                f.write(f"Sig({nt}) = {{{', '.join(sorted(resultados_siguiente[i][nt]))}}}\n")


gramaticas = leer_lagramatica('glcs.in')
resultados_primero = []
resultados_siguiente = []

for producciones in gramaticas:
    simbolo_inicial = list(producciones.keys())[0]
    primeros = calcular_todos_los_primeros(producciones)
    siguientes = calcular_todos_los_siguientes(producciones, primeros, simbolo_inicial)
    resultados_primero.append(primeros)
    resultados_siguiente.append(siguientes)

escribir_resultados('pr_sig.out', gramaticas, resultados_primero, resultados_siguiente) #escribe en el archivo.out
