import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
import Instagram_send_dm as dms
from datetime import datetime
import traceback

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

main_ui = Ui_MainWindow()
NAME = 'Mirae Makers'



# --------------------------------------------------------------------------------------------------------------------





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        main_ui.setupUi(self)     
        self.show()
        self.setWindowTitle(NAME)

        window_ico = resource_path('favicon.ico')
        self.setWindowIcon(QIcon(window_ico))

        self.ids = []
        self.pwds = []
        self.sending_ids = []
        self.PATH_IMG = None


        main_ui.btn_get_ids.clicked.connect(self.btn_get_idsClicked)
        main_ui.btn_add_2.clicked.connect(self.btn_add_2Clicked)
        main_ui.btn_del_2.clicked.connect(self.btn_del_2Clicked)


        main_ui.send_num.textChanged.connect(self.send_num_isnumber)
        main_ui.delay.textChanged.connect(self.delay_isnumber)

        
        main_ui.btn_get_sending_ids.clicked.connect(self.btn_get_sending_idsClicked)
        main_ui.btn_del_sending_id.clicked.connect(self.btn_del_sending_idClicked)
        main_ui.btn_clear_sending_ids.clicked.connect(self.btn_clear_sending_idsClicked)

        main_ui.btn_get_image.clicked.connect(self.btn_get_imageClicked)
        main_ui.btn_del_image.clicked.connect(self.btn_del_imageClicked)
        main_ui.btn_start_2.clicked.connect(self.btn_start_2Clicked)



# --------------------------------------------------------------------------------------------------------------------


   
    def btn_get_idsClicked(self):
        path = QFileDialog.getOpenFileNames(self)    
        for i in path[0]:
            try:
                if i == '':
                    return 
                file = open(i, 'rt', encoding='UTF8')
                
                while True:
                    line = file.readline()
                    if not line:
                        break
                    elif line == '\n':
                        continue
                    line = line.strip().split(' ')
                    if line[0] in self.ids:
                        continue
                    self.ids.append(line[0])
                    self.pwds.append(line[1])
                    main_ui.ids.addItem(line[0] + '\t' + line[1])
            except:
                j = i.split('/')[-1]
                QMessageBox.information(self,NAME,f'{j} 파일 내용이 잘못되었습니다.')
                return 
        
    def btn_add_2Clicked(self):
        id = main_ui.id_2.text()
        pwd = main_ui.pwd_2.text()

        if all([id, pwd]):
            self.ids.append(id)
            self.pwds.append(pwd)
            main_ui.ids.addItem(id + '\t' + pwd)
            main_ui.id_2.clear()
            main_ui.pwd_2.clear()
        return 

    def btn_del_2Clicked(self):
        if main_ui.ids.currentItem():
            tmp = main_ui.ids.currentRow()
            main_ui.ids.takeItem(main_ui.ids.currentRow())
            self.ids.remove(self.ids[tmp])
            self.pwds.remove(self.pwds[tmp])


    def send_num_isnumber(self):
        if main_ui.send_num.text().isdecimal():
            return
        else:
            if main_ui.send_num.text() == '': return
            main_ui.send_num.setText('')
            QMessageBox.information(self,NAME,'계정 당 발송 수는 숫자만 가능합니다.')
            return

    def delay_isnumber(self):
        if main_ui.delay.text().isdecimal():
            return
        else:
            if main_ui.delay.text() == '': return
            main_ui.delay.setText('')
            QMessageBox.information(self,NAME,'발송 딜레이는 숫자만 가능합니다.')
            return


    def btn_get_sending_idsClicked(self):
        path = QFileDialog.getOpenFileNames(self)    
        for i in path[0]:
            try:
                if i == '':
                    return 
                file = open(i, 'rt', encoding='UTF8')
                
                while True:
                    line = file.readline()
                    if not line:
                        break
                    elif line == '\n':
                        continue
                    elif line.strip() in self.sending_ids:
                        continue
                    self.sending_ids.append(line.strip())
                    main_ui.seding_ids.addItem(line.strip())
            except:
                j = i.split('/')[-1]
                QMessageBox.information(self,NAME,f'{j} 파일 내용이 잘못되었습니다.')
                return 
        return

    def btn_del_sending_idClicked(self):
        if main_ui.seding_ids.currentItem():
            tmp = main_ui.seding_ids.currentRow()
            main_ui.seding_ids.takeItem(main_ui.seding_ids.currentRow())
            self.sending_ids.remove(self.sending_ids[tmp])
        return
    
    def btn_clear_sending_idsClicked(self):
        option = QMessageBox.warning(self, NAME, "정말로 초기화하시겠습니까?", QMessageBox.Yes | QMessageBox.No)
        if option == QMessageBox.Yes:
            self.sending_ids = []
            main_ui.seding_ids.clear()
        else:
            return
    
    
    def btn_get_imageClicked(self):
        extension = ['png', 'jpg', 'jpeg', 'gif']
        image_path = QFileDialog.getOpenFileName(self)  
        if image_path[0] == '':
            return     
        if image_path[0].split('.')[-1] in extension:
            self.PATH_IMG = image_path[0]
            main_ui.img.setText(self.PATH_IMG)
            self.PATH_IMG = self.PATH_IMG.replace("/", "\\")
        else:
            QMessageBox.information(self,NAME,'확장자는 png, jpg, jpeg, gif만 사용 가능합니다.')
            
        return
    
    def btn_del_imageClicked(self):
        self.PATH_IMG = None
        main_ui.img.setText('')
        return

    def btn_start_2Clicked(self):
        send_num = main_ui.send_num.text()
        delay = main_ui.delay.text()

        cmt = main_ui.cmt_2.toPlainText()
        if cmt.replace('\n', '').replace(' ', '') == '':
            cmt = None
        

        if self.ids: pass
        else:
            QMessageBox.information(self,NAME, '로그인 아이디 정보가 없습니다.')
            return
        
        if self.sending_ids: pass
        else:
            QMessageBox.information(self,NAME, '불러온 아이디 정보가 없습니다.')
            return
        
        if send_num: pass
        else: 
            QMessageBox.information(self,NAME, '계정 당 발송 수를 정해주세요.')
            return
        
        if delay: pass
        else: 
            QMessageBox.information(self,NAME, '발송 딜레이를 정해주세요.')
            return
        

        if any([self.PATH_IMG, cmt]):
            try:
                dms.start_dm(int(send_num), [self.ids, self.pwds], self.sending_ids, int(delay), self.PATH_IMG, cmt)
                QMessageBox.information(self,NAME, 'DM 발송이 완료되었습니다.')
            except Exception as ex:
                date = datetime.now().strftime("%Y-%m-%d_%H%M%S")
                file = open(f"ex_{date}.txt", "w")
                err_msg = traceback.format_exc()
                file.write(err_msg)
                file.close()
                QMessageBox.information(self,NAME, '프로그램이 예상치 못한 이유로 종료되었습니다.')
            return
            
        else:
            QMessageBox.information(self,NAME, '원고나 이미지 둘 중 하나는 작성되어야 합니다.')
            return
        



    
# ---------------------------------------------------------------------------------------------------------------------------


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

