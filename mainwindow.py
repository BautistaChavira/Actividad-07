from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
from Particulas import Particula
from Listas import Lista

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.lista = Lista()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.click_agregar)
        self.ui.pushButton.clicked.connect(self.click_final)
        self.ui.pushButton_3.clicked.connect(self.click_mostrar)
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
        
        
    @Slot()
    def action_abrir_archivo(self):
      
       ubicacion = QFileDialog.getOpenFileName(
        self,
        'Abrir archivo',
        '.',
        'JSON (*.json)'
       )[0]
       if self.lista.abrir_archivo(ubicacion):
          self.ui.plainTextEdit.clear()
          self.ui.plainTextEdit.insertPlainText("Lista cargada\n")
          self.ui.plainTextEdit.insertPlainText(str(self.lista))
          QMessageBox.information(
            self,
            "Carga completada",
            "Se cargaron los datos contenidos en :" + ubicacion
          )
       else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo" + ubicacion
        )

    @Slot()
    def action_guardar_archivo(self):
      ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar',
            '.',
            'JSON (*.json)'
        )[0]
      print(ubicacion)
      if self.lista.guardar_archivo(ubicacion):
        QMessageBox.information(
            self,
            "Guardado completado",
            "Se pudo crear el archivo en la direccion : " + ubicacion,
            
        )

      else :
        QMessageBox.critical(
            self,
            "ERROR",
            "NO SE PUDO CREAR EL ARCHIVO" + ubicacion
        )

    @Slot()
    def click_mostrar(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.lista))

    @Slot()
    def click_agregar(self):
        id = self.ui.spinBox.value()
        origen_x = self.ui.spinBox_2.value()
        origen_y = self.ui.spinBox_3.value()
        destino_x = self.ui.spinBox_4.value()
        destino_y = self.ui.spinBox_5.value()
        velocidad = self.ui.spinBox_6.value()
        rojo = self.ui.spinBox_7.value()
        verde = self.ui.spinBox_8.value()
        azul = self.ui.spinBox_9.value()

        particula = Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,rojo,verde,azul)
        self.lista.insertar_inicio(particula)

    @Slot()
    def click_final(self):
        id = self.ui.spinBox.value()
        origen_x = self.ui.spinBox_2.value()
        origen_y = self.ui.spinBox_3.value()
        destino_x = self.ui.spinBox_4.value()
        destino_y = self.ui.spinBox_5.value()
        velocidad = self.ui.spinBox_6.value()
        rojo = self.ui.spinBox_7.value()
        verde = self.ui.spinBox_8.value()
        azul = self.ui.spinBox_9.value()

        particula = Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,rojo,verde,azul)
        self.lista.insertar_final(particula)