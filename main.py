# This one doesn't work on replit
#Use an IDE on your local computer with graphics

from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout
from PyQt6.QtWidgets import QLabel,QPushButton,QLineEdit,QComboBox
from PyQt6.QtCore import Qt
from pathlib import Path

def open_files():
  global filenames
  filenames, _ = QFileDialog.getOpenFileNames(window, 'Select files')
  message.setText('\n'.join(filenames))

def destroy_files():
  for filename in filenames:
    path=Path(filename)
    with open(path, 'wb') as file:
      file.write(b'') # Not sure this destroys a file
    path.unlink()
  message.setText('Destruction Successful')


app=QApplication([])
window=QWidget()
window.setWindowTitle('File Destroyer')
layout=QVBoxLayout()

description=QLabel('Select the files you want to destroy.  The fileswill be <font color="red">permanently</font> deleted')
layout.addWidget(description)

open_btn=QPushButton('Open Files')
open_btn.setToolTip('File tool to select the files')
open_btn.setFixedWidth(100)
layout.addWidget(open_btn,alignment=Qt.Alignment.AlignCenter)
open_btn.clicked.connect(open_files)

destroy_btn=QPushButton('Destroy files')
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn,alignment=Qt.Alignment.AlignCenter)
open_btn.clicked.connect(destroy_files)

message=QLabel('')
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec()

