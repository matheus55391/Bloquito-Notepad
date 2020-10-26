# By: Matheus55391
# -*- coding: utf-8 -*- 

from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys

"""
    Meu primeiro bloco de notas em python :)
    @Autor: Meguinha - Matheus Felipe Vieira Santiago
    
"""

class Bloquito(QMainWindow):
  

    def __init__(self):

        super().__init__()
        self.savepath = None
        self.winconfig()
        self.initUI()
        self.show()
        

    def winconfig(self):
        #configuracoes da janela 
        self.setWindowIcon(QtGui.QIcon('assets/icon.png'))
        self.setWindowTitle('Bloquito')
        self.resize(800,600)
        
        
    def topbarmenu(self):
        #-----------------------------------------------------
        #                 � _�  TopBar � _�                     -
        #-----------------------------------------------------
        btn_new  = self.menuBar().addAction('New')
        btn_open = self.menuBar().addAction('Open')
        btn_save = self.menuBar().addAction('Save')        
        
        btn_new.triggered.connect (self.btn_new_Action )
        btn_open.triggered.connect (self.btn_open_Action)
        btn_save.triggered.connect  (self.btn_save_Action)

    def initUI(self): 
        #-----------------------------------------------------
        #  ♡╰(*´︶`*)╯ horizontal layout box ╰(*´︶`*)╯♡     -
        #     Configuracoes das janelas principal            -
        #     Aqui é onde carregamos de fato a interface     -
        #     Widgets e layouts                              -
        #-----------------------------------------------------
        self.topbarmenu()

        self.textEdit = QPlainTextEdit() #editor de texto
        self.textEdit.setStyleSheet("background-color: #f8f8ff")

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(self.textEdit) 
        container = QWidget()
        container.setLayout(vbox_layout)
        self.setCentralWidget(container)

    #----------------------------------------
    #  ♡(⌒▽⌒) Acoes da topbar (⌒▽⌒)♡    -
    #----------------------------------------
    def btn_new_Action(self):
        #  Quando apertar o botão new na topbar.
        #  Abre uma nova janela.
        print('new')
        try:
            self.nw = Bloquito()
            self.nw.show()
        except:
            print("Erro event_new")

    def btn_open_Action(self):
        # Quando apertar o botão open na topbar.
        #Faz a leitura de um arquivo
        #similar ao event_save
        #Apenas faz leitura limpa o qtextedit e cola o que tem no arquivo por cima.
        
        file_path = QFileDialog.getOpenFileName(self)
        self.savepath = file_path[0]
        self.setWindowTitle(f"{self.savepath} - Bloquito")
        print(self.textEdit.toPlainText())

        try:
            with open(f'{self.savepath}', 'r') as textfile:

                data = textfile.read() # armazena os dados do arquivo lido
                self.textEdit.clear()
                self.textEdit.setPlainText(data)
        except:
            pass


    def btn_save_Action(self):
        #  Quando apertar o botão save na topbar
        #  Salva o arquivo
        print('save')
        try:
            if self.savepath == None:
                file_path = QFileDialog.getSaveFileName(self, "Save File Window Title", "defualt.txt", "All Files(*)")
                self.savepath = file_path[0]
            self.setWindowTitle(f"{self.savepath} - Bloquito")
            with open(f'{self.savepath}', 'w') as file:
                file.write(self.textEdit.toPlainText())

        except:
            pass



def main():
    
    app = QApplication(sys.argv)
    ex = Bloquito()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


