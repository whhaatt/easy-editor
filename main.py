#створи тут фоторедактор Easy Editor!
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget,QFileDialog,
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout,
)
app = QApplication([])
main_win = QWidget()
main_win.resize(700, 500)
main_win.setWindowTitle('My_Proga')
lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папка")
main_files = QListWidget()
btn_left = QPushButton("Вліво")
btn_right = QPushButton("Право")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")
btn_flip = QPushButton("Зеркало")
row = QHBoxLayout()
row2 = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(main_files)
col2.addWidget(lb_image)
row2.addWidget(btn_left)
row2.addWidget(btn_right)
row2.addWidget(btn_flip)
row2.addWidget(btn_sharp)
row2.addWidget(btn_bw)
col2.addLayout(row2)
row.addLayout(col1)
row.addLayout(col2)
main_win.setLayout(row)
main_win.show()

workdir = ''

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def filter(files, extansions):
def showFilenamesList():

btn_dir.clicked.connect(showFilenamesList)





app.exec_()