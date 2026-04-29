import random as rand
#186
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QCheckBox
)
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import Qt, QEvent, QObject
import sys

# --- BACKEND STUFFS ---

# temporary key for testing. it's SUPPOSED to be uppercase. do not edit!
dekey = [('a','C'), ('b','L'), ('c','T'), ('d','H'), ('e','A'),
           ('f','N'), ('g','V'), ('h','W'), ('i','Z'), ('j','Y'),
           ('k','S'), ('l','K'), ('m','R'), ('n','P'), ('o','M'),
           ('p','O'), ('q','D'), ('r','I'), ('s','X'), ('t','F'),
           ('u','B'), ('v','J'), ('w','E'), ('x','G'), ('y','U'),
           ('z','Q')]
key=dekey
def changekey(keystr):
    key=[]
    for i in range(26):
        key.append((f'{dekey[i][0]}', f'{keystr[i]}'), )


#for i in range(len(key)):
#    key[i]=f"['{dekey[i][0]}', '{key[i][0]}']"


print(key)
print()
print(dekey)

#print(dekey)
#print(key)

def spacer(h, p): # adds a space at a location in a string. this exists solely for legibility.
    return h[:p] + " " + h[p:]

def encode(key, entry, patristocrat):
    result = entry.lower()
    for (i,j) in key:
       result = result.replace(i,j)
    result = result.lower()
    if patristocrat:
        result = result.replace(" ","")
        #for y in range(5, len(result)+6, 6):
        for y in range(5, len(result)*2, 6):
            result = spacer(result,y)
    return result.strip()


def decrypt(key, entry):
    result = []
    
    dictKey = dict(key)
    #reverse dictionary
    dictKey = {v.lower(): k for k, v in dictKey.items()}

    entry = entry.lower()
    entry = list(entry)
    
    for j in range(len(entry)):
        if entry[j] in dictKey:
            result.append(dictKey[entry[j]])
        else:
            result.append(entry[j])
    
    return ''.join(result)



# --- TESTING ---

#patr_toggle = 0 # patristocrat toggle; change to a toggle in the GUI later

#print(encode(testkey,input("Phrase to encode: "),patr_toggle)) # encoder call

#print(decode(testkey,input("Phrase to decode: "),patr_toggle)) # gorg decoder call

#alphabet = set('abcdefghijklmnopqrstuvwxyz')
#userkey = input("Please input your key: ") # in the GUI later, note that the case is not preserved.
#while not (len(userkey) == 26 and alphabet.issubset(key)):
#    userkey = input("The key was the wrong length or it was missing characters please input a new key: ")

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
        self.short_box_style = """
            background-color: #181825;
            color: #a6adc8;
            font-size: 15pt;
            border-radius: 0.5em;
            max-height: 20px;
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
        self.textbox_subheaders = """
            font-size: 17pt;
        """
        
        # layout
        self.layout = QVBoxLayout(self)

        # entry box header
        self.entryheader = QLabel("Plaintext (letter case not preserved)")
        self.entryheader.setStyleSheet(self.textbox_headers)
        self.layout.addWidget(self.entryheader)

        # patristocrat note
        #self.patnote = QLabel("patristocrat mode:")
        #self.patnote.setStyleSheet("""
        #    font-weight: bold;
        #    font-size: 10pt;
        #""")
        #self.layout.addWidget(self.patnote)

        # patristocrat checkbox
        self.patcheck = QCheckBox("patristocrat mode")
        self.layout.addWidget(self.patcheck)

        # text entry box
        self.entrybox = QTextEdit()
        self.entrybox.setStyleSheet(self.rounded_box_style)
        self.entrybox.installEventFilter(self)
        self.layout.addWidget(self.entrybox)

        # button encode
        self.button = QPushButton("Encode!")
        self.button.clicked.connect(self.encoderInterface) # worried about this
        self.button.setStyleSheet(self.button_style)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.decryptInterface)

        # output box header
        self.outputheader = QLabel("Output")
        self.outputheader.setStyleSheet(self.textbox_headers)
        self.layout.addWidget(self.outputheader)

        # output box
        self.outputbox = QTextEdit()
        self.outputbox.setStyleSheet(self.rounded_box_style)
        self.outputbox.setReadOnly(1)
        self.layout.addWidget(self.outputbox)

        # center toggle
        #self.centercheck = QCheckBox("CenterStuff")
        #self.layout.addWidget(self.centercheck)
        #self.centercheck.toggled.connect(self.on_centercheck_toggled)

        # decryption toggle
        self.decryptcheck = QCheckBox("decrypt")
        self.layout.addWidget(self.decryptcheck)
        self.decryptcheck.toggled.connect(self.buttonchange)

        # TODO - input a custom key to use, instead of testkey.
        # should also decline all keys that don't contain
        # exactly 1 of each letter of the alphabet.

        # keybox header
        self.keyboxheader = QLabel("custom key")
        self.keyboxheader.setStyleSheet(self.textbox_subheaders)
        self.layout.addWidget(self.keyboxheader)

        # custom key / keybox
        self.keybox = QTextEdit()
        self.keybox.setStyleSheet(self.short_box_style)
        self.layout.addWidget(self.keybox)



    def decryptInterface(self):
        if self.decryptcheck.isChecked():
            textentry = self.entrybox.toPlainText().strip()
            decrypttext = decrypt(key, textentry)
            self.outputbox.setPlainText(decrypttext)
            #print(textentry) # again, no prints in main.

    # used for changing the text of the button 
    def buttonchange(self):
        if not self.decryptcheck.isChecked():
            self.button.setText("Encrypt!")
        else:
            self.button.setText("Decrypt!")

    #def on_centercheck_toggled(self, checked):
    #    if checked:
    #       self.entryheader.setAlignment(Qt.AlignCenter)
    #       self.outputheader.setAlignment(Qt.AlignCenter)
    #       print("stuff centered")
    #    else:
    #        self.entryheader.setAlignment(Qt.AlignLeft)
    #        self.outputheader.setAlignment(Qt.AlignLeft)

    def keyboxInterface(self):
        global dekey
        key = self.keybox.toPlainText().strip()
        for i in range(26):
            key=[]
            key.append((f'{dekey[i][0]}', f'{key[i]}'), )
        return key

    def encoderInterface(self):
        #global dekey

        #usekey = self.keyboxInterface()

        usekey = changekey(self.keybox.toPlainText().strip().upper())

        if not self.decryptcheck.isChecked():
            textentry = self.entrybox.toPlainText().strip()
            encodedtext = encode(key,textentry, self.patcheck.isChecked())

            self.outputbox.setPlainText(encodedtext)

    # keyboard shortcut to press enter to submit
    
    def eventFilter(self, obj, event):
        if obj is self.entrybox and event.type() == QEvent.Type.KeyPress:
            key = event.key()
            modifiers = event.modifiers()
            if key == Qt.Key.Key_Return:
                if modifiers & Qt.ShiftModifier:
                    return super().eventFilter(obj, event)
                elif self.entrybox.hasFocus():
                    if self.decryptcheck.isChecked():
                        self.decryptInterface()
                    else:
                        self.encoderInterface()
                    return 1

        #if obj is self.keybox and event.type() == QEvent.Type.KeyPress:
        #    key = event.key()
        #    modifiers = event.modifiers()
        #    if key == Qt.Key.Key_Return:
        #        changekey()
        #        if modifiers & Qt.ShiftModifier:
        #            return super().eventFilter(obj, event)
        #        elif self.keybox.hasFocus():
        #            return 1

            return super().eventFilter(obj, event)
        return super().eventFilter(obj, event)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cipherer()
    window.setStyleSheet("""
        color: #cdd6f4;
        background-color: #1e1e2e;
    """)
    window.resize(500, 600)
    window.show()
    sys.exit(app.exec())
