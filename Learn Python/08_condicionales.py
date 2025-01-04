### Condicionales ###

my_condition = True

if my_condition:
    print("Se ejecuta la condición del if")

print("La ejecución continúa")

my_other_condition = False

if my_other_condition:
    print("Se ejecuta la condición segundo del if")

my_condition = 5*2

if my_condition:
    print("Se ejecuta la condición del tercer if")

if my_condition == 11:
    print("Se ejecuta la condición del cuarto if")

if my_condition == 10:
    print("Se ejecuta la condición del quinto if")

if my_condition > 10: 
    print("Es mayor que 10")
else:
    print("Es menor o igual a 10")


my_condition = 5 * 5
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10  menor que 20")
else:
    print("Es menor o igual a 10 o mayor o igual que 20")


my_condition = 5 * 3
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 o menor que 20")
else:
    print("Es menor o igual a 10 o mayor o igual que 20")


    my_condition = 5 * 3
if my_condition > 10 and my_condition < 15:
    print("Es mayor que 10 y menor que 15")
elif my_condition >= 15 and my_condition <20:
    print("Es mayor o igual a 15 y menor que 20")
else:
    print("Es mayor o igual que 20")