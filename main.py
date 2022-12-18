from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QApplication

from matheese import Matheese

if __name__ == '__main__':
    app = QApplication([])
    matheese = Matheese()
    # load all icons and images
    ###################################
    icon = QIcon("resource/nailao.ico")
    app.setWindowIcon(icon) 
    ###################################
    pixmap = QPixmap("resource/matheese.png")
    matheese.ui.label.setPixmap(pixmap)
    ###################################
    #launch the application
    matheese.ui.show()
    app.exec()