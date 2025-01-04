"""
Cubos de 1 in y 5 in >= goal
"""
def test(small_bricks, big_briks, goal):
    if  (small_bricks + (big_briks * 5)) >= goal:
        return True 
    else:
        return False
        
print(test(3,0,5))

"""
string con triplets tres letras iguales seguidas
"""

def test2(string):
    list_string = list(string)
    cont = 0
    for i in range(0, len(list_string)-2):
        if list_string[i] == list_string[i + 1] == list_string[i + 2]:
            cont += 1
    if cont > 0:
        return True
    else:
        return False
    
print(test2("absXxx"))


""" 
24? cubos con 2 letras para formar palabras
"""
"""
def canGenerateWord(word, blocks):
    block_list = list(blocks.split(","))
    new_block = []
    for j in range(0, len(block_list)):
        sublist = []
        sublist[:0] = block_list[j]
        new_block.append(sublist)
    
    position = []

    for i in range(0, len(block_list)):
        for x in range(0,2):
            for w in word:
                if new_block[i][x] == w:
                    
                    position.append(i)
                    
    selected_blocks = list(set(position))

    if len(selected_blocks) >= len(word):
        return True
    else:
        return False
"""


def canGenerateWord(word, blocks):
    block_lst = []
    for j in blocks:
        blc = list(j)
        block_lst.append(blc)
        
    position = []

    for i in range(0, len(block_lst)):
        for x in range(0,2):
            for w in word:
                if block_lst[i][x] == w:
                    position.append(i)
    
    print(position)
    selected_blocks = list(set(position))
    print(selected_blocks)

    if len(selected_blocks) >= len(word):
        return True
    else:
        return False  


bricks = ["AN", "BD", "DC"]



print(canGenerateWord("ADN", bricks))
"""
print(bricks)

sublist = []
for j in bricks:
    blc = list(j)
    sublist.append(blc)
        
print(sublist)
"""
"""
strn="hola"
s = []
for w in strn:
    s.append(w)
    
print(s)
"""