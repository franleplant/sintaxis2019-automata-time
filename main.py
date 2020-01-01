TRAMPA = -1
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def delta(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "0":
        return 1
    if estado_anterior == 0 and caracter == "1":
        return 1
    if estado_anterior == 0 and caracter == "2":
        return 2
    if estado_anterior == 1 and caracter in digits:
        return 3
    if estado_anterior == 2 and caracter in ["0", "1", "2", "3"]:
        return 3 
    if estado_anterior == 3 and caracter == ":":
        return 4
    if estado_anterior == 4 and caracter in ["0", "1", "2", "3", "4", "5"]:
        return 5
    if estado_anterior == 5 and caracter in digits:
        return 6



    return TRAMPA

# automata
def pertenece(cadena):
    Finales = [6]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = delta(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO



casos = [
    ("13:00", RESULTADO_ACEPTADO),
    ("26:98", RESULTADO_TRAMPA),
    ("13", RESULTADO_NO_ACEPTADO),
    # "25",
    # "01",
]

for cadena, resultado in casos:
    print( (cadena, pertenece(cadena)) )
    assert pertenece(cadena) == resultado



