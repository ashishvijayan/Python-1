# -*- coding: utf-8 -*-
"""w8ppa5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x7_M042zwV55DlTaoCavvHK0c0t9-2UP
"""

def check_palindrome(word):
    
    if len(word) == 1:
        return True
    if len(word) == 2:
        if word[0] == word[1]:
            return True

    return word[0] == word[-1] and check_palindrome(word[1:-1])
check_palindrome('SAIPPUAKIVIKAUPPIAS')