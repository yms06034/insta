import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
import Instagram_get_user_ids as ids
import Instagram_send_dm as dms
from datetime import datetime


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




        self.ids2 = []
        self.pwds2 = []
        self.hashtags = []

        main_ui.btn_get_ids_2.clicked.connect(self.btn_get_ids_2Clicked)
        main_ui.btn_add_3.clicked.connect(self.btn_add_3Clicked)
        main_ui.btn_del_3.clicked.connect(self.btn_del_3Clicked)

        main_ui.hashtag.returnPressed.connect(self.addKeyword)
        main_ui.follower.textChanged.connect(self.follower_isnumber)
        main_ui.count.textChanged.connect(self.count_isnumber)

        main_ui.btn_add.clicked.connect(self.btn_addClicked)
        main_ui.btn_del.clicked.connect(self.btn_delClicked)
        

        main_ui.btn_get_hashtags.clicked.connect(self.btn_get_hashtagsClicked)
        main_ui.btn_clear_hashtags.clicked.connect(self.btn_clear_hashtagsClicked)

        main_ui.btn_start.clicked.connect(self.btn_startClicked)

 


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
        
        
        # if main_ui.ids.count() > 0:
        #     for i in range(main_ui.ids.count()):
        #         insta_id_list.append(main_ui.ids.item(i).text())
        # else: insta_id_list = None

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
        

        if all([self.PATH_IMG, cmt]):
            dms.start_dm(send_num, [self.ids, self.pwds], self.sending_ids, delay, self.PATH_IMG)
            return
            
            
        else:
            QMessageBox.information(self,NAME, '원고나 이미지 둘 중 하나는 작성되어야 합니다.')
            return
        



    
# ---------------------------------------------------------------------------------------------------------------------------

    def btn_get_ids_2Clicked(self):
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
                        if line[0] in self.ids2:
                            continue
                        self.ids2.append(line[0])
                        self.pwds2.append(line[1])
                        main_ui.ids_2.addItem(line[0] + '\t' + line[1])
                except:
                    j = i.split('/')[-1]
                    QMessageBox.information(self,NAME,f'{j} 파일 내용이 잘못되었습니다.')
                    return 
                
    def btn_add_3Clicked(self):
        id = main_ui.id.text()
        pwd = main_ui.pwd.text()

        if all([id, pwd]):
            self.ids2.append(id)
            self.pwds2.append(pwd)
            main_ui.ids_2.addItem(id + '\t' + pwd)
            main_ui.id.clear()
            main_ui.pwd.clear()
        return 

    def btn_del_3Clicked(self):
        if main_ui.ids_2.currentItem():
            tmp = main_ui.ids_2.currentRow()
            main_ui.ids_2.takeItem(main_ui.ids_2.currentRow())
            self.ids2.remove(self.ids2[tmp])
            self.pwds2.remove(self.pwds2[tmp])

    def addKeyword(self):
        if main_ui.hashtag.text().replace(' ', ''):
            if main_ui.hashtag.text().replace(' ', '') in self.hashtags:
                main_ui.hashtag.clear()
                return
            self.hashtags.append(main_ui.hashtag.text().replace(' ', ''))
            main_ui.hashtags.addItem(main_ui.hashtag.text())
            main_ui.hashtag.clear()
        return

    def follower_isnumber(self):
        if main_ui.follower.text().isdecimal():
            return
        else:
            if main_ui.follower.text() == '': return
            main_ui.follower.setText('')
            QMessageBox.information(self,NAME,'팔로워 수는 숫자만 가능합니다.')
            return
        
    def count_isnumber(self):
        if main_ui.count.text().isdecimal():
            return
        else:
            if main_ui.count.text() == '': return
            main_ui.count.setText('')
            QMessageBox.information(self,NAME,'추출 개수는 숫자만 가능합니다.')


    def btn_addClicked(self):
        self.addKeyword()
        return

    def btn_delClicked(self):
        if main_ui.hashtags.currentItem():
            self.hashtags.remove(self.hashtags[main_ui.hashtags.currentRow()])
            main_ui.hashtags.takeItem(main_ui.hashtags.currentRow())
        return 

    def btn_get_hashtagsClicked(self):
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
                    elif line.replace(' ', '').replace('\n','') in self.hashtags:
                        continue
                    main_ui.hashtags.addItem(line.replace(' ', '').replace('\n',''))
                    self.hashtags.append(line.replace(' ', '').replace('\n',''))
            except:
                j = i.split('/')[-1]
                QMessageBox.information(self,NAME,f'{j}파일 내용이 잘못되었습니다.')
                return 
        return

    def btn_clear_hashtagsClicked(self):
        option = QMessageBox.warning(self, NAME, "정말로 초기화하시겠습니까?", QMessageBox.Yes | QMessageBox.No)
        if option == QMessageBox.Yes:
            main_ui.hashtags.clear()
            self.hashtags.clear()
        return


    def btn_startClicked(self):
        follow = None
        count = None

        if all([self.ids2, self.pwds2]): pass
        else:
            QMessageBox.information(self,NAME, '아이디와 비밀번호를 입력해주세요.')
            return

        if self.hashtags == []:
            QMessageBox.information(self,NAME, '1개 이상의 해시태그를 입력해주세요.')
            return
            
        if main_ui.follower.text():
            follow = main_ui.follower.text()
        else:
            follow = None

        if main_ui.count.text():
            count = main_ui.count.text()
        else:
            count = None

        if all([self.ids2, self.pwds2, self.hashtags, follow, count]):
            main_ui.id_list.clear()
            rt, user_ids = ids.get_user_ids(self.ids2, self.pwds2, self.hashtags, int(count), int(follow))
            
            n = 0
            for i in user_ids:
                n += len(i)
            main_ui.total_num.setText(f'{n} 개')
            try:
                for i in range(len(user_ids)):
                    main_ui.id_list.addItem('['+self.hashtags[i]+']')
                    main_ui.id_list.addItems(user_ids[i])
                    main_ui.id_list.addItem('')
            except: 
                main_ui.id_list.addItem('아이디 추출 중에 오류가 발생하였습니다.\ntxt파일을 확인해주세요.') 
            self.hashtags = []
            main_ui.hashtags.clear()
            self.browser = None
        else:
            QMessageBox.information(self,NAME,'빈칸을 모두 채워주세요.')
            return


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

