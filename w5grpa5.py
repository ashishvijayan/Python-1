# -*- coding: utf-8 -*-
"""w5grapa5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qDp_xCQFg55Y4auGSqR4U_y7leAamKVT
"""

def tra(m):
    trnsps = []
    for r in range(len(m[0])):
        l = []
        for c in range(len(m)):
            l.append(m[c][r])
        trnsps.append(l)
    return trnsps
m = [[4, 3], [9, 5], [2, 7]]
tra(m)