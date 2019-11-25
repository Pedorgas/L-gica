from PyQt5.QtWidgets import (QApplication, Qlabel, QVBoxLayout, QtWidget, QLineEdit, QPushButton, QMessageBox)

from PyQt5.QtCore import pyqtSlot

from test import limpador_de_cpf

@pyqtSlot()
def verificarCPF():
    alerta = QMessageBox()
    cpf_digitado = cpf.text()
    cpf_limpo = limpador_de_cpf(cpf_digitado)
    alerta.setText("CPF digitado foi: " + cpf_digitado)
    alerta.exec_()


app = QApplication([])
janela = QtWidget()
layout = QVBoxLayout()

titulo = Qlabel("Meu verificador de CPF")
layout.addWidget(cpf)
botao1 = QPushButton("verificar CPF")
botao1.clicked.connect(verificarCPF)
layout.addWidget(botao1)
janela.setLayout(layout)

janela.show()
app.exec_()
