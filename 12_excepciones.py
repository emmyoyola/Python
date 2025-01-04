### Manejo de xcepciones ###

number_one, number_two = 5, 1
print(number_one + number_two)

number_two = "1"
# print(number_one + number_two) Esto es un error

# try, exept

try:
    print(number_one + number_two)
    print("No se ha producido error")
except: # Se ejecuta si se produce una excepción
    print("Se ha producido un error")


# try, except, else

try:
    print(number_one + number_two)
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else: # Se ejecuta si no se produce una excepción
    print("La ejcución continúa correctamente")


# try, except, else, finally

try:
    print(number_one + number_two)
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else:
    print("La ejcución continúa correctamente")
finally:
    print("La ejecución continúa")


# Excepciones por tipo

try:
    print(number_one + number_two)
    print("No se ha producido error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")


# Captura de la información de la excepción 

"""try:     # Este mostraría un error
    print(number_one + number_two)
    print("No se ha producido error")
except ValueError as error:
    print(error)
"""

try:
    print(number_one + number_two)
    print("No se ha producido error")
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)



