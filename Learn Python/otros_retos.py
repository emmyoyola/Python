# NÚMEROS PRIMOS

def weird_number(n):
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n in range(2, 6):
        print("Not Weird")
    elif n % 2 == 0 and n in range(6, 21):
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
    else:
        print("Weird")
            
weird_number(3)
weird_number(24)
weird_number(4)
weird_number(6)

print(list(range(4)))
print(["1", "2"])


# STRING DE NÚMEROS

def consecutive(n):
    lista = []
    for i in range(1, n + 1):
        string = str(i)
        lista.append(string)
    number = ''.join(lista)
    print(number)

consecutive(7)


# AÑOS BISIESTOS

def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True       
    return leap

print(is_leap(2024))


# CUBO COORDENADAS

"""let's learn about list comprehensions! You are given three integers x, y and z
representing the dimensions of a cuboid along with an integer n.
Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k
is not equal to n. 
Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z . 
Please use list comprehensions rather than multiple loops, as a learning exercise"""

def cubo(x, y, z, n):
    lst=[[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n] 
    print(lst)
    
cubo(1, 1, 2, 3)


#SUBCAMPEÓN


