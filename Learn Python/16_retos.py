### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ"

 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 """
 
 
def fizz_buzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("FizzBuzz")
        elif index % 3 == 0:
            print("Fizz")
        elif index % 5 == 0:
            print("Buzz")
        else:
            print(index)
        
fizz_buzz()


"""
¿ES UN ANAGRAMA?

Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word1, word2):
    if word1.lower() == word2.lower():
        return False
    return sorted(word1.lower()) == sorted(word2.lower())

print(is_anagram("Amor", "Roma"))
print(is_anagram("Amor", "roma"))
print(is_anagram("Amor", "Amor"))
print(is_anagram("Amor", "amor"))
print(is_anagram("Maria", "Airma"))
print(is_anagram("Hola", "Ola"))


"""
LA SUCESIÓN DE FIBONACCI

Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    
    prev = 0    # Inicializar
    next = 1
    
    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next  
        next = fib
        
fibonacci()


"""
¿ES UN NÚMERO PRIMO?

Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""