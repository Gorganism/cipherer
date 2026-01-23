        # layout
        self.layout = QVBoxLayout(self)

        # entry box header
        self.entryheader = QLabel("Plaintext (letter case not preserved)")
        self.entryheader.setStyleSheet(self.textbox_headers)
        self.layout.addWidget(self.entryheader)

        # patristocrat note
        # self.patnote = QLabel("patristocrat mode:")
        # self.patnote.setStyleSheet("""
        #     font-weight: bold;
        #     font-size: 10pt;
        # """)
        # self.layout.addWidget(self.patnote)

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

        '''
        # center toggle
        self.centercheck = QCheckBox("CenterStuff")
        self.layout.addWidget(self.centercheck)
        self.centercheck.toggled.connect(self.on_centercheck_toggled)
        '''
        # decryption toggle thing
        self.decrypt = QCheckBox("Toggle between decrypt and encrypt")
        self.layout.addWidget(self.decrypt)
        self.decrypt.toggled.connect(self.buttonchange)


        # TODO - patristocrat toggle (like a checkbox or something,
        # changes the `patristocrat` variable to be 1 or 0)

        # TODO - input a custom key to use, instead of testkey.
        # should also decline all keys that don't contain 1 of
        # each letter of the alphabet.


    def decryptInterface(self, checked):
        if self.decrypt.isChecked():
            textentry = self.entrybox.toPlainText().strip()
            decrypttext = decrypt(testkey, textentry)
            self.outputbox.setPlainText(decrypttext)
            print(textentry)

     # used for changing the text of the button 
    def buttonchange(self):
        if self.decrypt.isChecked():
            self.button.setText("Encrypt!")
        else:
            self.button.setText("Decrypt!")

    '''
    def on_centercheck_toggled(self, checked):
        if checked:
            self.entryheader.setAlignment(Qt.AlignCenter)
            self.outputheader.setAlignment(Qt.AlignCenter)
            print("stuff centered")
        else:
            self.entryheader.setAlignment(Qt.AlignLeft)
            self.outputheader.setAlignment(Qt.AlignLeft)
    '''

    def encoderInterface(self, checked):
        global testkey # temporary

        if not self.decrypt.isChecked():
            textentry = self.entrybox.toPlainText().strip()
            encodedtext = encode(testkey,textentry, self.patcheck.isChecked())

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
                    return 1
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
