import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from fatorial import Ui_MainWindow  # Importa a interface gerada

class main_exerc03(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conectar o botão à função que realiza a soma
        self.ui.pushButton.clicked.connect(self.fatorial)
    
    def fatorial(self):
        try:
            # Ler os números dos campos de entrada
            num = int(self.ui.lineEditnum1.text())
            
            fatorial = 1
            for i in range(1, num + 1):
                fatorial *= i
            self.ui.textEdit.setText(f"{fatorial}")
        except ValueError:
            self.ui.textEdit.setText("Por favor, insira números válidos!")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_exerc03()
    janela.show()
    sys.exit(app.exec_())

