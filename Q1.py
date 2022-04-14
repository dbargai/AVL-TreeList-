import avl_skeleton as AVLTreeList
import random 
######## First Exp - Insertions ########
for i in range (1, 11):
    experimental = AVLTreeList.AVLTreeList()
    cnt = experimental.insert("0",0)
    print(cnt)
    for j in range (1000*(2**i)):
        r = random.randint(0,experimental.length()-1)
        cnt += experimental.insert(r, str(r))
    print ("For tree with 1000*2^",i,"nodes, number of 'Balance Ops' is:", cnt)

