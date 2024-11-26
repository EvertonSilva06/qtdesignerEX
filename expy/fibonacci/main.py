import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from fibonacci import Ui_MainWindow  # Importa a interface gerada

class main_fibonnaci(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.fibonnaci)
        
    def fibonnaci(self):
        num1 = int(self.ui.lineEditnum1.text())
        a, b = 0, 1
        sequencia = []

        for _ in range(num1):
            sequencia.append(str(a))
            a, b = b, a + b
            
        self.ui.textEdit.setText(f"Resultado: {sequencia}")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_fibonnaci()
    janela.show()
    sys.exit(app.exec_())