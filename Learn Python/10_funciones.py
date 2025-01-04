### Funciones ###

def my_function():
    print("Esto es una fn")

my_function()

def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(3, 5)

def sum_two_values_with_return(first_number, second_number):
    return first_number + second_number

my_result = sum_two_values_with_return(3, 36)    #Asigno el resultado de una fn a una variable
print(my_result)

def sum_two_values_with_return(first_number, second_number):
    my_sum = first_number + second_number
    return my_sum

sum_two_values_with_return(2,4)
print(sum_two_values_with_return(2,4))

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname = "Oyola", name = "Emmy")    # Reordenar parámetros

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Emmy", "Oyola") # En este caso imprime el valor por defecto

def print_texts (*text):    # El asterísco indica que puedo pasar varios valores
    print(text)
 
print_texts("Hola", "Mundo")

