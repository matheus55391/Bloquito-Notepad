#Nesse arquivo estou testando uma barra superior para o bloco de notas

import sys
from PyQt5.QtWidgets import *


class Mw(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
     
        

        menubar = self.menuBar()
        event_new  = menubar.addMenu('New')
        event_open = menubar.addMenu('Open')
        event_save = menubar.addMenu('Save')

        self.vbox = QVBoxLayout()



        
        
        self.setWindowTitle('TopBarTestefrom PyQt5.QtWidgets import QMainWindow')
        self.show()


    
def main():
    app = QApplication(sys.argv)
    ex = Mw()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()