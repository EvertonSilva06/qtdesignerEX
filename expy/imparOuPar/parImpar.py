import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from imparOuPar import Ui_MainWindow  # Importa a interface gerada

class main_exerc02(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conectar o botão à função que realiza a soma
        self.ui.pushButton.clicked.connect(self.impar_par)
    
    def impar_par(self):
        try:
            # Ler os números dos campos de entrada
            num = int(self.ui.lineEditnum1.text())
            
            if num % 2 == 0:
                self.ui.textEdit.setText("O número é par.")
            else:
                self.ui.textEdit.setText("O número é ímpar.")

        except ValueError:
            self.ui.textEdit.setText("Por favor, insira números válidos!")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_exerc02()
    janela.show()
    sys.exit(app.exec_())

