from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QStyle, QMainWindow
from PyQt5.QtWinExtras import QtWin
import project_cust_38.Cust_Qt as CQT
CQT.conver_ui_v_py()
from untitled import Ui_MainWindow  # импорт нашего сгенерированного файла
import project_cust_38.Cust_Functions as F
import sys
import os


class mywindow(QMainWindow):
    resized = QtCore.pyqtSignal()
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.showMaximized()
        self.ui.le_path_base.textChanged[str].connect(self.base_path_ico)


    def load_table(self):
        if not F.nalich_file(self.ico_pack_path):
            CQT.msgbox(f'Не найдена папка ')
            sys.exit()

        list_icons = F.spis_files(self.ico_pack_path)[0][2]
        spis = [['img','name']]
        for i in range(len(list_icons)):
            spis.append(['',list_icons[i]])

        tbl = self.ui.tbl
        CQT.fill_wtabl(spis,tbl,min_width_col=64)
        for i in range(1, len(spis)):
            CQT.add_image(tbl,i-1,0,self.ico_pack_path+ F.sep() + spis[i][1],'',64,64)
            tbl.setRowHeight(i-1,64)

        self.ui.btn_ok.clicked.connect(self.ok)

    def base_path_ico(self,path):
        if F.nalich_file(path):
            self.ico_pack_path = path
            self.load_table()

    def ok(self):
        if self.ui.tbl.currentRow() == -1:
            return
        name_ico = self.ui.tbl.item(self.ui.tbl.currentRow(),1).text()
        #ras = F.ostavit_rasshir(name_ico)
        ras  =''
        path= self.ui.le_path.text()
        if not F.nalich_file(path):
            CQT.msgbox(f'Не найден путь')
            return
        name = self.ui.le_name.text()
        if name == '':
            CQT.msgbox(f'Имя пусто')
            return
        full_path = F.sep().join((path,name)) + ras

        if F.nalich_file(full_path):
            if not CQT.msgboxgYN(f'{full_path} уже существует, заменить?'):
                return
            F.udal_file(full_path)
        F.skopir_file(self.ico_pack_path + name_ico, full_path)
        CQT.msgbox(f'ОК', time_life=0.5)





app = QtWidgets.QApplication(sys.argv)

args = sys.argv[1:]
myappid = 'Powerz.BAG.SystCreateWork.1.0.3'  # !!!
QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
app.setWindowIcon(QtGui.QIcon(os.path.join("icons", "1.ico")))


application = mywindow()
application.show()
sys.exit(app.exec())