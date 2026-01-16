import random as rand
# from PySide6.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
# )
# from PySide6.QtGui import QTextCursor
# from PySide6.QtCore import Qt, QEvent, QObject
alphabet = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y',
            'z']
# --- User input ---
key = input("Please input your key ")
key = list(key)
while len(key) != 26 and not alphabet.issubset(other)::
            key = input("The key was the wrong length or it was missing characters please input a new key")

# --- BACKEND STUFFS ---

# temporary key for testing
testkey = [('a','c'), ('b','l'), ('c','t'), ('d','h'), ('e','a'),
           ('f','n'), ('g','v'), ('h','w'), ('i','z'), ('j','y'),
           ('k','s'), ('l','k'), ('m','r'), ('n','p'), ('o','m'),
           ('p','o'), ('q','d'), ('r','i'), ('s','x'), ('t','f'),
           ('u','b'), ('v','j'), ('w','e'), ('x','g'), ('y','u'),
           ('z','q')]

def encode():
    for (i,j)


def decrypt(alph,key,encrypted): # TODO change a couple variable names like epic because that does not make sence
    encrypted=list(encrypted)
    for i in range(len(encrypted)):
        p=-1
        epic="hi"
        while epic != encrypted[i]:
            p+=1
            epic=key[p][1]
            print(epic)
            if encrypted[i]==" ":
                result.append(" ")
                break
        if encrypted[i]==" ":
            print("added space to the list")
        else:
            result.append(key[p][0])
        print(result)
    print("".join(result))

            
# TODO - finish backend and allat

# --- FRONTEND ---

# class Interface(QWidget):
#     def __init__(self):
#         super().__init__()
#         # TODO - stuff here for UI
