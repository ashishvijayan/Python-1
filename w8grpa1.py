# -*- coding: utf-8 -*-
"""w8grpa1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x7_M042zwV55DlTaoCavvHK0c0t9-2UP
"""

def reverse(L):
    if L == []:
        return []
    
    else:
        new = []
    
        new.append(L[-1])
    
        L.remove(L[-1])
        #print('new:', new)
        #print('L:', L)
        return new + reverse(L)
reverse([1,2,3])
