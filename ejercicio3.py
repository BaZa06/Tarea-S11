#Ejercicio 3: Calcular la suma de los dígitos de un número elevado a una potencia
#Planteamiento: Crea una función que reciba dos parámetros: un número entero positivo y un exponente. 
# La función debe calcular el número elevado al exponente dado, luego sumar todos los dígitos del resultado y devolver esa suma. 
# Por ejemplo, si el número es 2 y el exponente es 3, calcula  2^3 = 8, y la suma de los dígitos es 8. Si el número es 5 y el exponente es 2, 
# calcula 5^2 = 25, y la suma de los dígitos es 2 + 5 = 7.

def suma_numeros_potencia(numero1, numero2):
    if numero1 and numero2 == 0:
        return 1
    elif numero1 and numero2 == 1:
        return 1
    else:
        resultado = numero1 ** numero2
        suma_resultado = sum(int(digit) for digit in str(resultado))
        return suma_resultado
    
while True:
    numero1 = int(input("Ingrese un número entero positivo: "))
    numero2 = int(input("Ingrese un número entero y positivo como exponente: "))
    try:
        numero1_valido = int(numero1)
        numero2_valido = int(numero2)
        if numero1 and numero2 < 0 :
            print("Los número deben de ser positivos y enteros")
        else:
            break
    except ValueError:
        print("Por favor, ingrese número que sean enteros y postivos: ")
        
print(f"El número {numero1} elevado a la potencia {numero2} es: {numero1 ** numero2}")
print(f"La suma de los dígitos de {numero1} elevado a la potencia {numero2} es: {suma_numeros_potencia(numero1, numero2)}")