from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout,QGridLayout, QTextEdit
from bloquito.utils import setColor

"""
    Meu primeiro bloco de notas em python :)
    @Autor: Meguinha - Matheus Felipe Vieira Santiago
    
"""



class Bloquito(QWidget):
    

    def __init__(self):
        super().__init__()
        self.savepath = None
        self.setWindowTitle("Bloquito")
        self.setStyleSheet("background-color: 	#2fb7c2; ")
        self.resize(800,600)
        self.initUI()
        
    def initUI(self):
        
        
        #----------------------------------------
        #         ಠ_ಠ  Botões  ಠ_ಠ
        #----------------------------------------


        self.textbox = QTextEdit()
        setColor(self.textbox, "#f8f8ff")
        #----------------------------------------
        #  ♡╰(*´︶`*)╯ horizontal layout box ╰(*´︶`*)╯♡
        #----------------------------------------
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)

        
        #----------------------------------------
        #  ♡(⌒▽⌒) vertical layoutbox (⌒▽⌒)♡
        #----------------------------------------
        self.vbox = QVBoxLayout()
        self.hbox.addStretch(1)
        self.setLayout(self.vbox)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.textbox)

    def event_open(self):
        print("open event")
        #Faz a leitura de um arquivo
        #similar ao event_save
        #Apenas faz leitura limpa o qtextedit e cola o que tem no arquivo por cima.
        
        file_path = QFileDialog.getOpenFileName(self)
        self.savepath = file_path[0]
        self.setWindowTitle(f"Bloquito - {self.savepath}")
        print(self.textbox.toPlainText())

        try:
            with open(f'{self.savepath}', 'r') as textfile:

                data = textfile.read() # armazena os dados do arquivo lido
                self.textbox.clear()
                self.textbox.setPlainText(data)
        except:
            pass

       
        
    def event_new(self):
        #abre uma nova janela
        try:
            self.nw = Bloquito()
            self.nw.show()
        except:
            print("Erro event_new")


    def event_save(self):
        # Evento de salvar o con
        try:
            if self.savepath == None:
                file_path = QFileDialog.getSaveFileName(self, "Save File Window Title", "defualt.txt", "All Files(*)")
                self.savepath = file_path[0]
            self.setWindowTitle(f"Bloquito - {self.savepath}")
            with open(f'{self.savepath}', 'w') as file:
                file.write(self.textbox.toPlainText())

        except:
            pass



    
