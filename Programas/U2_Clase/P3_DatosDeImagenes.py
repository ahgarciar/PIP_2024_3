import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P3_DatosDeImagenes.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals

        self.lista_imagenes = {
            1: ":/Logos/FIT_logo_vertical.png",
            2: ":/Logos/log_uat_nuevo.png",
            3: ":/Personajes/ImagenGatoEuropeo.png",
            4: ":/Personajes/gato.jpeg"
        }
        self.clave_imagen = 1 ##primera imagen a mostrar
        self.imagen.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.clave_imagen]))
        self.btn_atras.clicked.connect(self.atras)
        self.btn_adelante.clicked.connect(self.adelante)

    # Área de los Slots
    def atras(self):
        print(self.clave_imagen)
        if self.clave_imagen >= 2:
            self.clave_imagen -= 1
            self.imagen.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.clave_imagen]))
    def adelante(self):
        print(self.clave_imagen)
        if self.clave_imagen < 4:
            self.clave_imagen += 1
            self.imagen.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.clave_imagen]))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

