### Cadenas ###

string_tabulado = "\tString tabulado"
print(string_tabulado)

string_escapado = "String \nescapado"
print(string_escapado)

# Formateo

name, surname, age = "Emmy", "Oyola", 23
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")
print("Mi edad es", age)

# Desempaqueteado de carácteres

language = "Python"
a, b, c, d, e, f= language

print(a)
print(b)

# División

language_slice = language[1:3]
print(language_slice)

inverso = language[-1]
print(inverso)

reversed_language = language[::-1]