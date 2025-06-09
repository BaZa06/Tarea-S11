#Ejercicio 2: Convertir un número decimal a binario
#Planteamiento: Escribe una función que reciba un número entero positivo y devuelva una cadena con su representación en binario (base 2).
# Por ejemplo, si se ingresa 10, la función debe devolver "1010". No uses funciones integradas de conversión a binario; 
# implementa la lógica dividiendo el número y construyendo la cadena manualmente.

def numero_a_binario(numero):
    if numero < 0:
        return "El numero debe ser postivo"
    elif numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2
    return binario

numero_binario = int(input("Ingrese un número entero positivo: "))
numero_base = numero_a_binario(numero_binario)

print(f"El resultado de convertir el número {numero_binario} a binario es: {numero_base}")