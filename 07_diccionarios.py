### Dicccionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Emmy", "Apellido":"Oyola", "Edad": 23, 1:"Python"}
print(my_other_dict)
print(type(my_other_dict))

my_dict = {
    "Nombre":"Emmy", 
    "Apellido":"Oyola", 
    "Edad": 23, 
    "Lenguaje":{"Python","swift", "Kotlin"} # Clave:str, Valor: Set
    }

print(my_dict)

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro" # Puedo cambiar el valor de una clave
print(my_dict["Nombre"])

my_dict["Estatura"] = 1.64 # Agregar un nuevo elemento
print(my_dict)

print("Oyola" in my_dict) # Falso ya que se está usando el valor  no la clave
print("Apellido" in my_dict) # FEsto es correcto, True

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = my_dict.fromkeys(("Nombre","Apellido","Piso")) # Crea un nuevo diccionario pero no importa si las claves pertenecen a my_dict
print(my_new_dict)