import numpytuto as np

a = np.array([12,3,4,5])
print(a)
print(a[::2])
print(a[:2])
print(a.dtype)
a = np.array([12,3,4,5], dtype = float)
print(a.dtype)
print([i * 5 for i in a])

print("EJEMPLO B")
b = np.array([
 #    0 1 2 3   
    [[1,2,3,4], #0
     [1,2,5,6]], #1  #0
    
    [[3,4,6,7],     
     [1,3,6,7]],    #1
    
    [[1,2,3,4],
     [1,3,4,5]]     #2
    ])
print(b.shape)
print(b.ndim)
print(b.size)
print(b[2][1][3])   #dim:2, fil:1, col:3
print(b[0, 1, 1])   #dim:0, fil:1, col:1
print(b[0:2])       #dim:0 y 1
print(b[:,0,:])     # de todas las dimensiones traer la fila 0 con todas sis columnas
print("Here")
print(b.sum(axis=2))

print("EJEMPLO C")
c = np.array([
    [1,2,3,4],
    [2,3,4,6],
    [6,8,9,4]
    ])

print(c.sum())
print(c.mean())
print(c.std())
print(c.var())
print(c.sum(axis=0))

print("EJEMPLO D")
d = np.arange(4)
print(d)
print(d + 10)
print(d * 2)
d += 10
print(d)

print("EJEMPLO E,F")
e = np.array([1,45,4,75])
f = np.arange(2,6)
print(e+f)

# Boolean arrays
print("EJEMPLO G")
g = np.arange(4)
print(g)
print(g[0], g[-1])
print(g[[0,-1]])
print(g[[True,False,False,True]])
print(g >=2)
print(g[g >=2])
print(g[g > g.mean()])
print(g[~(g > g.mean())])   # (~)no que no son mayores que la media
print(g[(g == 0) | ( g == 3)])
print(g[(g <= 2) & ( g % 2 == 0)])

print("EJEMPLO H")
h = np.random.randint(100, size=(3,3))
print(h)
print(h[np.array([
    [True, False, True],
    [False, True, True],
    [True, True, False]
    ])])
print(h > 30)


print("EJEMPLO I,J")
i = np.random.randint(100, size=(3,3))
print(i)
j = np.random.randint(100, size=(3,2))
print(j)
print(i.dot(j))
print(i @ j)
print(j.T)






