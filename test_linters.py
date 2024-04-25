# Función para calcular la suma de los primeros n números naturales
def suma_naturales(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma


# Calcular la suma de los primeros 10 números naturales
resultado = suma_naturales(10)
print("La suma de los primeros 10 números naturales es:", resultado)
