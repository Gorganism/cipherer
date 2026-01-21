import random as rand
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
)
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import Qt, QEvent, QObject
import sys

# --- BACKEND STUFFS ---

# temporary key for testing. it's SUPPOSED to be uppercase. do not edit!
testkey = [('a','C'), ('b','L'), ('c','T'), ('d','H'), ('e','A'),
           ('f','N'), ('g','V'), ('h','W'), ('i','Z'), ('j','Y'),
           ('k','S'), ('l','K'), ('m','R'), ('n','P'), ('o','M'),
           ('p','O'), ('q','D'), ('r','I'), ('s','X'), ('t','F'),
           ('u','B'), ('v','J'), ('w','E'), ('x','G'), ('y','U'),
           ('z','Q')]


def spacer(h, p): # adds a space at a location in a string. this exists solely for legibility.
    return h[:p] + " " + h[p:]

def encode(key, entry, patristocrat):
    result = entry
    for (i,j) in key:
       result = result.replace(i,j)
    result = result.lower()
    if patristocrat:
        result = result.replace(" ","")
        for y in range(5, len(result)+6, 6):
            result = spacer(result,y)
    return result


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


# gorg's version of the decoder tool:

# def decode(key, entry, patristocrat):
#     result = entry
#     for (i,j) in key:
#        result = result.replace(j.lower(),i.upper())
#     result = result.lower()
#     if patristocrat:
#         result = result.replace(" ","")
#     return result


# --- TESTING ---

patr_toggle = 0 # patristocrat toggle; change to a toggle in the GUI later

# print(encode(testkey,input("Phrase to encode: "),patr_toggle)) # encoder call

# print(decode(testkey,input("Phrase to decode: "),patr_toggle)) # gorg decoder call

# alphabet = set('abcdefghijklmnopqrstuvwxyz')
# userkey = input("Please input your key: ") # in the GUI later, note that the case is not preserved.
# while not (len(userkey) == 26 and alphabet.issubset(key)):
#     userkey = input("The key was the wrong length or it was missing characters please input a new key: ")

# --- FRONTEND / UI ---

class Cipherer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cipherer")
        self.rounded_box_style = """
            background-color: #181825;
            color: #a6adc8;
            font-size: 15pt;
            border-radius: 0.5em;
            padding: 0.5em;
        """
        self.button_style = """
            background-color: #f2cdcd;
            color: #1e1e2e;
            font-weight: bold;
            font-size: 15pt;
            border-radius: 0.5em;
            padding: 0.5em;
        """
        self.textbox_headers = """
            font-weight: bold;
            font-size: 20pt;
        """
        
        # layout
        self.layout = QVBoxLayout(self)

        # entry box header
        self.entryheader = QLabel("Plaintext (letter case not preserved)")
        self.entryheader.setStyleSheet(self.textbox_headers)
        self.layout.addWidget(self.entryheader)

        # text entry box
        self.entrybox = QTextEdit()
        self.entrybox.setStyleSheet(self.rounded_box_style)
        self.entrybox.installEventFilter(self)
        self.layout.addWidget(self.entrybox)

        # button
        self.button = QPushButton("Encode!")
        self.button.clicked.connect(self.encoderInterface) # worried about this
        self.button.setStyleSheet(self.button_style)
        self.layout.addWidget(self.button)

        # output box header
        self.outputheader = QLabel("Output")
        self.outputheader.setStyleSheet(self.textbox_headers)
        self.layout.addWidget(self.outputheader)

        # output box
        self.outputbox = QTextEdit()
        self.outputbox.setStyleSheet(self.rounded_box_style)
        self.outputbox.setReadOnly(True)
        self.layout.addWidget(self.outputbox)

        # TODO - patristocrat toggle (like a checkbox or something,
        # changes the `patristocrat` variable to be 1 or 0)

        # TODO - input a custom key to use, instead of testkey.
        # should also decline all keys that don't contain 1 of
        # each letter of the alphabet.


    def encoderInterface(self):
        global testkey # temporary

        textentry = self.entrybox.toPlainText().strip()
        encodedtext = encode(testkey,textentry,1)

        self.outputbox.setPlainText(encodedtext)

    # shortcut to press enter to submit
    
    def eventFilter(self, obj, event):
        if obj is self.entrybox and event.type() == QEvent.Type.KeyPress:
            key = event.key()
            modifiers = event.modifiers()
            if key == Qt.Key.Key_Return:
                if modifiers & Qt.ShiftModifier:
                    return super().eventFilter(obj, event)
                elif self.entrybox.hasFocus():
                    self.encoderInterface()
                    return True
            return super().eventFilter(obj, event)
        return super().eventFilter(obj, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cipherer()
    window.resize(500, 600)
    window.show()
    sys.exit(app.exec())
