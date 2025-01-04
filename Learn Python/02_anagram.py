"""
¿ES UN ANAGRAMA?

Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

word_one="Palabra"
word_two="abralaP"

ana1 = list(word_one)
ana2 = list(word_two)

print(ana1 == ana2)
b = list(word_one.lower())
b.sort()
print(b)


def is_anagram(word1, word2):

    w1 = list(word1.lower())
    w2 = list(word2.lower())
    w1.sort()
    w2.sort()
    
    if word1.lower() == word2.lower():
        return False
    elif w1 == w2:
        return True
    return False
 
print(is_anagram("Amor", "Roma"))
print(is_anagram("Amor", "roma"))
print(is_anagram("Amor", "Amor"))
print(is_anagram("Amor", "amor"))
print(is_anagram("Maria", "Airma"))
print(is_anagram("Hola", "Ola"))