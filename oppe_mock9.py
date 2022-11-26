# -*- coding: utf-8 -*-
"""oppe_mock9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eTf40H_w8PbZPLGnuNFsmXYe68Q_fzN0
"""

def coins(order):
    '''
    There are five boxes arranged from left to right. You keep adding a variable number of coins sequentially in each box. 
    Start from box-1 and keep going right. Once you reach the last box, head back to box-1 and then keep adding coins.
    In any given turn, the number of coins added to a box is always less than 10.
    Find the box which has the maximum number of coins. If there are two boxes which have the same maximum number of coins,
    output the smaller of the two box numbers. The sequence of coins is represented by a string. 
    '''
    l = list()
    for num in order:
        num = int(num)
        l.append(num)
    print(l)
    
    m = len(l)
    if m % 5 == 0:
        
        new = [0,0,0,0,0]
        low = 0
        high = 0
    

        for i in range(0,m,5):
            #print('i=',i)
            low = i
            high = low+5
        
            l1 = l[low:high]
            new = [sum(n) for n in zip(*[l1, new])]

    else:
        while len(l)%5 != 0:
            l.append(0)

        new = [0,0,0,0,0]
        low = 0
        high = 0
    

        for i in range(0,m,5):
            #print('i=',i)
            low = i
            high = low+5
        
            l1 = l[low:high]
            new = [sum(n) for n in zip(*[l1, new])]
        
        
    max = new[0]
    max_index = 0
    for i in range(1,len(new)):
        if new[i] > max:
            max = new[i]
            max_index = i

    print(new)    
    return max_index+1

order = '12345123456'     
coins(order)
