import random as rand
# from PySide6.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
# )
# from PySide6.QtGui import QTextCursor
# from PySide6.QtCore import Qt, QEvent, QObject

# --- TESTING ---

alphabet = set('abcdefghijklmnopqrstuvwxyz')
userkey = input("Please input your key: ")
while not (len(userkey) == 26 and alphabet.issubset(key)):
    userkey = input("The key was the wrong length or it was missing characters please input a new key: ")

# --- BACKEND STUFFS ---

# temporary key for testing
testkey = [('a','c'), ('b','l'), ('c','t'), ('d','h'), ('e','a'),
           ('f','n'), ('g','v'), ('h','w'), ('i','z'), ('j','y'),
           ('k','s'), ('l','k'), ('m','r'), ('n','p'), ('o','m'),
           ('p','o'), ('q','d'), ('r','i'), ('s','x'), ('t','f'),
           ('u','b'), ('v','j'), ('w','e'), ('x','g'), ('y','u'),
           ('z','q')]

def encode(key, entry):
    result = entry
    for (i,j) in result:
       result = result.replace(i,j)
    
    result = result.lower()
    # TODO finish this

def decrypt(alph,key,encrypted): # TODO change a couple variable names like epic because that does not make sense
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
    return ("".join(result))

            
# TODO - finish backend and allat

# --- FRONTEND ---

# class Interface(QWidget):
#     def __init__(self):
#         super().__init__()
#         # TODO - stuff here for UI
