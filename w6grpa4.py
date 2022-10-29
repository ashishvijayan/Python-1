# -*- coding: utf-8 -*-
"""w6grpa4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qDp_xCQFg55Y4auGSqR4U_y7leAamKVT
"""

def two_level_sort(scores):
    '''
    Write a function named two_level_sort that accepts a list of tuples named scores as argument. 
    Each element in this list is of the form (Name, Marks) and represents the marks scored by a student in a test: 
    the first element is the student's name and the second element is his or her marks.

    The function should return a list of tuples sorted that is sorted in two levels:

    Level-1: ascending order of marks
    Level-2: alphabetical order of names among those students who have scored equal marks
    Each element in the returned list should also be of the form (Name, marks). 
    Note that level-2 should not override level-1. That is, after the second level of sorting, 
    the list should still be sorted in ascending order of marks. Additionally, the students having the same marks 
    should appear in alphabetical order

    '''

    def first_level(scores):

        ascend = [scores[0]]

        for i in range(1,len(scores)):
            flag = True
            for j in range(len(ascend)):
                if scores[i][1] <= ascend[j][1]:
                    beforej = ascend[:j]
                    afterj = ascend[j:]
                    insert = [scores[i]]
                    ascend = ascend[:j] + [scores[i]] + ascend[j:]
                    flag = False
                    break
            if flag:
                ascend.append(scores[i])
        return ascend

    ascend = first_level(scores)

    for i in range(len(ascend)):
        empty = ()
        for j in range(i+1,len(ascend)):
            if ascend[j][1] == ascend[i][1]:
                if ascend[j][0] < ascend[i][0]:
                    empty = ascend[i]
                    ascend[i] = ascend[j]
                    ascend[j] = empty

    return ascend

                                      
scores = [('Harsh', 80), ('Harsh', 90), ('Harsha', 80), ('Harsha',90), ('Sachin', 70), ('Sam', 69), ('Anirudh', 70), ('Anita', 80), ('z', 100), ('y', 90), ('x', 80), ('d', 50), ('a', 20)]	


print(two_level_sort(scores))
