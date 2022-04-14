from cmath import exp
from tkinter import E
import avl_skeleton as AVLTreeList
import random 
import sys
def exp1():
    ###### First Exp - Insertions ########
    for i in range (1, 11):
        experimental = AVLTreeList.AVLTreeList()
        cnt = experimental.insert(0, "0")
    # Insert 1000*2^i nodes randomly
        for j in range (1000*(2**i)-1):
            r = random.randint(0,experimental.length()-1)
            cnt += experimental.insert(r, str(r))
        print ("For tree with 1000*2^",i,"nodes, number of 'Balance Ops' is:", cnt)

#exp1()


def exp2():
    ####### Second Exp - Deletions ########
    for i in range (1, 11):
        experimental = AVLTreeList.AVLTreeList()
        experimental.insert(0, "0")
    # Insert 1000*2^i nodes randomly
        for j in range (1000*(2**i)-1):
            r = random.randint(0,experimental.length()-1)
            experimental.insert(r, str(r))
        cnt=0
    # Delete all nodes in a random order: 
        for k in range (1000*(2**i)):
            r = random.randint(0,experimental.length()-1)
            cnt += experimental.delete(r)
        print ("For tree with 1000*2^",i,"nodes, number of 'Balance Ops' is:", cnt)

#exp2()


def exp3():
    ###### Third Exp - Insertions/Deletions ########
    for i in range (1, 11):
        experimental = AVLTreeList.AVLTreeList()
        experimental.insert(0, "0")
    # Insert 1000*2^i nodes randomly
        w = 1000*(2**(i-1))-1
        for j in range (1000*(2**(i-1))-1):
            r = random.randint(0,experimental.length()-1)
            experimental.insert(r, str(r))
            print(experimental.length())
        cnt=0
        w = experimental.length()
        for k in range (int(1000*(2**(i-2)))):
            if experimental.length()!=(1000*(2**(i-1))):
                print(r)
                return [experimental, r]
            try:
                r = random.randint(0,experimental.length()-1)
                cnt += experimental.insert(r, str(r))
                r = random.randint(0,experimental.length()-1)
                cnt += experimental.delete(r)
            except Exception:
                o = sys.exc_info()
        print ("For tree with 1000*2^",i,"nodes, number of 'Balance Ops' is:", cnt)

problem = exp3()
problem[0].delete(problem[1])