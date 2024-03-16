def encriptar_cadena(cadena):
    # Diccionario de encriptación
    encriptacion = {
        'L': '$', 'V': '%', 'E': 'R', 'B': 'Y',
        'A': '7', 'I': '#', 'S': 'Q', 'D': '&',
        ' ': ' '  # Mantenemos el espacio como está
    }

    # Lista para almacenar la cadena encriptada
    cadena_encriptada = []

    # Lista para almacenar las posiciones de cada token
    posiciones = []

    # Convertir la cadena a mayúsculas
    cadena = cadena.upper()

    # Iterar sobre cada carácter en la cadena
    for idx, caracter in enumerate(cadena):
        if caracter in encriptacion:
            cadena_encriptada.append(encriptacion[caracter])
            posiciones.append(idx)
        else:
            cadena_encriptada.append('N')
            posiciones.append(idx)

    # Mostrar la posición de cada token
    print("Posiciones de los tokens en el arreglo de salida:")
    for pos in posiciones:
        print(pos, end=' ')
    print()  # Nueva línea

    # Mostrar cantidad de caracteres
    print("Cantidad de caracteres:", len(cadena))

    # Mostrar la conversión de la cadena de entrada
    print("Conversión de la cadena de entrada:")
    print(''.join(cadena_encriptada))


# Ejemplo de uso
entrada = "la vida es bella"
encriptar_cadena(entrada)
