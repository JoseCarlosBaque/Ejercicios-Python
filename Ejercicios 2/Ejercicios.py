print( "Ej 1 ")
def suma_pares(numeros):
    suma_impar = 0
    for num in numeros:
        if num % 2 != 0:
            suma_impar += num
    return suma_impar 

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultados = suma_pares(numeros)
print("Suma pares:", resultados)

print( "Ej 2 ")
def elementos_unicos(lista):
    settear_lista = set(lista)
    lista_unica = list(settear_lista)
    return lista_unica

    lista_original = [1, 2, 2, 3, 4, 4, 5]
    resultados = elementos_unicos(lista_original)
    print(resultados)




print( "Ej 3 ")
def elementos_unicos_en_orden(lista):
    lista_unica = []
    mismos_elementos = set()

    for elemento in lista:
        if elemento not in mismos_elementos:
            mismos_elementos.add(elemento)
            lista_unica.append(elemento)

    return lista_unica

lista_original = [1, 2, 2, 3, 4, 4, 5]
resultados = elementos_unicos_en_orden(lista_original)
print(resultados)

print( "Ej 4 ")
def get_even_numbers(lista):
    num_pares = []
    for numeros in lista:
        if numeros % 2 == 0:
            num_pares.append(numeros)
    return num_pares

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultados = get_even_numbers(lista_original)
print(resultados)

print( "Ej 5 ")
def impares(input_list):
    even_numbers = []
    for number in input_list:
        if number % 2 != 0:
            even_numbers.append(number)
    return even_numbers

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultados = impares(lista_original)
print(resultados)

print( "Ej 6 ")
def n_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True

def numeros_primos(lista):
    num_primos = [num for num in lista if n_primo(num)]
    return num_primos

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultados = numeros_primos(lista_original)
print(resultados)

print( "Ej 7 ")
def palindromo(num):
    num_str = str(num)
    return num_str == num_str[::-1]

def num_palindromos(lista):
    numeros = [num for num in lista if palindromo(num)]
    return numeros

lista_original = [1, 2, 3, 10, 11, 12, 13, 14, 22, 23, 33, 44, 55, 66, 77, 88, 99, 101, 111, 252, 262, 292, 300, 301]
resultados = num_palindromos(lista_original)
print(resultados)
