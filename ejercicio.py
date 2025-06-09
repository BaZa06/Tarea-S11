#Ejercicio 1: Calcular el factorial de un número
#Planteamiento: Crea una función que reciba un número entero no negativo como parámetro y devuelva su factorial. 
# El factorial de un número n es el producto de todos los enteros positivos desde 1 hasta n (por ejemplo, 5! = 5 * 4 * 3 2   1 = 120).
# Asegúrate de manejar el caso especial donde n = 0, que devuelve 1.



def factorial_numero(n):
    if n == 0:
        return 1
    else:
        return n * factorial_numero(n - 1)
    
while True:
    numero = int(input("Ingrese un número entero positivo: "))
    try:
        numero_válido = int(numero)
        if numero_válido < 0:
            print("El numero debe de ser positivo y entero")
        else:
            break
    except ValueError:
        print("Por favor, ingres un número entero positivo:")
    
print(f"El factorial del {numero} es: {factorial_numero(numero)}")
