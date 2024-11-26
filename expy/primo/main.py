import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from primo import Ui_MainWindow  # Importa a interface gerada

class main_primo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.primo)
        
    def primo(self):
        num = int(self.ui.lineEditnum1.text())
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    self.ui.textEdit.setText("Não é primo")
                    break
            else:
                self.ui.textEdit.setText("é primo")
        else:
            self.ui.textEdit.setText("Não é primo")

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_primo()
    janela.show()
    sys.exit(app.exec_())