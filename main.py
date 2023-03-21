import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow, QRadioButton
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtWebEngineWidgets import QWebEngineView
import buttonsfunction

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle('YouQT')
window.setWindowIcon(QIcon('./image/Icon.ico'))
window.setMinimumSize(700, 500)
pal = window.palette()
pal.setColor(QPalette.Window, Qt.black)
window.setPalette(pal)


# url = "https://www.youtube.com/embed/CRe1zItxDsw?rel=0"
def playvideo():
    url1 = buttonsfunction.buttons().getVideo()
    url = url1
    print(url)
    player.load(QUrl(url))
# print(url)
player = QWebEngineView()
# player.load(QUrl(url))
playvideo()
#try:
# url1 = function.buttons().getVideo()
# url = url1
# player.load(QUrl(url))
# except:
#     "You've reached your daily request limit!"

central_widget = QWidget()
window.setCentralWidget(central_widget)

# anyBtn = QRadioButton("Any")
# anyBtn.setChecked(True)
# anyBtn.toggled.connect(lambda: function.buttons.anydura())
anyBtn = QPushButton('Any')
anyBtn.clicked.connect(lambda: buttonsfunction.buttons.anydura())

shortBtn = QPushButton('Short')
shortBtn.clicked.connect(lambda: buttonsfunction.buttons.shortdura())

mediumBtn = QPushButton('Medium')
mediumBtn.clicked.connect(lambda: buttonsfunction.buttons.mediumdura())

longBtn = QPushButton('Long')
longBtn.clicked.connect(lambda: buttonsfunction.buttons.longdura())

nextBtn = QPushButton('Next')
nextBtn.clicked.connect(lambda: playvideo())


hboxLayout = QHBoxLayout()
hboxLayout.setContentsMargins(0, 0, 0, 0)
hboxLayout.addWidget(anyBtn)
hboxLayout.addWidget(shortBtn)
hboxLayout.addWidget(mediumBtn)
hboxLayout.addWidget(longBtn)
hboxLayout.addWidget(nextBtn)


layout = QVBoxLayout(central_widget)
layout.addWidget(player)
layout.addLayout(hboxLayout)


window.show()

try:
    sys.exit(app.exec_())
except SystemExit:
    print('App closed! Watch again later.')
