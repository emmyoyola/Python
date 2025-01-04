### Listas ###

my_list = [35, 24, 62, 52, 30, 30, 17]
my_other_list = list()  #lista vacía

print(len(my_list))
print(my_list)

my_other_list = [23, 1.64, "Emmy", "Oyola"]
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list.count("Emmy"))
print(my_list.count(30))

age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list)

my_other_list.append("Hi")
print(my_other_list)

my_other_list.insert(2, "Gris")
print(my_other_list)

my_list.remove(30) # Sólo elimina el primer elemento
print(my_list)

print(my_list.pop()) # Imprime el último elemento (y lo elimina al mismo tiempo)

my_list.pop() # Elimina el último elemento
print(my_list)

print(my_list.pop(2)) # Imprime el elemento indicado (y lo elimina al mismo tiempo)
print(my_list)

my_new_list = my_list.copy() # Copia de mi lista
my_list.clear() # Limpiar la lista

print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[0:2])

print(my_other_list)
print(my_other_list.index("Emmy"))


