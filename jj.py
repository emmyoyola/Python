def canGenerateWord(word, blocks):
    block_list = list(blocks.split(","))
    new_block = []
    for j in range(0, len(block_list)):
        sublist = []
        sublist[:0] = block_list[j]
        new_block.append(sublist)
    
    position = []
    cont = 0
    lenBlock = len(new_block) 
    isPossible = True
    
    for w in word:
        for x in range (0,2):
            bool = False
            for i in range(0, len(block_list)):
                cont+=1   
                if new_block[i][x] == w:
                    bool = True               
                    position.append(i)
                if cont%(lenBlock*2) == 0 and not bool:
                    isPossible = False
                    
    selected_blocks = list(set(position))
    if not isPossible:
        print("no es posible")
        return False
    elif isPossible and len(selected_blocks) >= len(word):
        print("es posible")
        return True
    else:
        print("No es posible por longitud")
        return False
        
        
    
bricks = "AN,BD,DC"
#bricks = "AN,DO,NE,ND,MA"

print(canGenerateWord("ADN", bricks))