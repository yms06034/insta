# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 485)
        MainWindow.setMinimumSize(QtCore.QSize(590, 485))
        MainWindow.setMaximumSize(QtCore.QSize(590, 485))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 571, 455))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setGeometry(QtCore.QRect(280, 0, 131, 41))
        self.label_24.setObjectName("label_24")
        self.btn_add_2 = QtWidgets.QPushButton(self.tab)
        self.btn_add_2.setGeometry(QtCore.QRect(170, 80, 41, 31))
        self.btn_add_2.setObjectName("btn_add_2")
        self.btn_del_sending_id = QtWidgets.QPushButton(self.tab)
        self.btn_del_sending_id.setGeometry(QtCore.QRect(430, 180, 41, 30))
        self.btn_del_sending_id.setObjectName("btn_del_sending_id")
        self.img = QtWidgets.QLineEdit(self.tab)
        self.img.setGeometry(QtCore.QRect(280, 400, 211, 20))
        self.img.setReadOnly(True)
        self.img.setObjectName("img")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 60, 41))
        self.label_9.setObjectName("label_9")
        self.label_26 = QtWidgets.QLabel(self.tab)
        self.label_26.setGeometry(QtCore.QRect(10, 300, 91, 41))
        self.label_26.setObjectName("label_26")
        self.seding_ids = QtWidgets.QListWidget(self.tab)
        self.seding_ids.setGeometry(QtCore.QRect(280, 30, 271, 141))
        self.seding_ids.setObjectName("seding_ids")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(10, 330, 81, 41))
        self.label_23.setObjectName("label_23")
        self.cmt_2 = QtWidgets.QTextEdit(self.tab)
        self.cmt_2.setGeometry(QtCore.QRect(280, 240, 271, 131))
        self.cmt_2.setObjectName("cmt_2")
        self.btn_clear_sending_ids = QtWidgets.QPushButton(self.tab)
        self.btn_clear_sending_ids.setGeometry(QtCore.QRect(479, 180, 71, 30))
        self.btn_clear_sending_ids.setObjectName("btn_clear_sending_ids")
        self.delay = QtWidgets.QLineEdit(self.tab)
        self.delay.setGeometry(QtCore.QRect(80, 340, 181, 20))
        self.delay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.delay.setObjectName("delay")
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(280, 210, 131, 41))
        self.label_25.setObjectName("label_25")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(280, 370, 41, 41))
        self.label_22.setObjectName("label_22")
        self.ids = QtWidgets.QListWidget(self.tab)
        self.ids.setGeometry(QtCore.QRect(10, 123, 250, 176))
        self.ids.setObjectName("ids")
        self.send_num = QtWidgets.QLineEdit(self.tab)
        self.send_num.setGeometry(QtCore.QRect(100, 310, 161, 20))
        self.send_num.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.send_num.setObjectName("send_num")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(10, 75, 60, 41))
        self.label_21.setObjectName("label_21")
        self.btn_start_2 = QtWidgets.QPushButton(self.tab)
        self.btn_start_2.setGeometry(QtCore.QRect(10, 370, 251, 51))
        self.btn_start_2.setObjectName("btn_start_2")
        self.btn_del_2 = QtWidgets.QPushButton(self.tab)
        self.btn_del_2.setGeometry(QtCore.QRect(220, 80, 41, 31))
        self.btn_del_2.setObjectName("btn_del_2")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 60, 41))
        self.label_10.setObjectName("label_10")
        self.id_2 = QtWidgets.QLineEdit(self.tab)
        self.id_2.setGeometry(QtCore.QRect(70, 20, 191, 20))
        self.id_2.setObjectName("id_2")
        self.pwd_2 = QtWidgets.QLineEdit(self.tab)
        self.pwd_2.setGeometry(QtCore.QRect(70, 50, 191, 20))
        self.pwd_2.setObjectName("pwd_2")
        self.btn_get_ids = QtWidgets.QPushButton(self.tab)
        self.btn_get_ids.setGeometry(QtCore.QRect(70, 80, 91, 31))
        self.btn_get_ids.setObjectName("btn_get_ids")
        self.btn_get_sending_ids = QtWidgets.QPushButton(self.tab)
        self.btn_get_sending_ids.setGeometry(QtCore.QRect(280, 180, 141, 31))
        self.btn_get_sending_ids.setObjectName("btn_get_sending_ids")
        self.btn_get_image = QtWidgets.QPushButton(self.tab)
        self.btn_get_image.setGeometry(QtCore.QRect(490, 390, 31, 31))
        self.btn_get_image.setObjectName("btn_get_image")
        self.btn_del_image = QtWidgets.QPushButton(self.tab)
        self.btn_del_image.setGeometry(QtCore.QRect(520, 390, 31, 31))
        self.btn_del_image.setObjectName("btn_del_image")
        self.label_24.raise_()
        self.btn_add_2.raise_()
        self.btn_del_sending_id.raise_()
        self.img.raise_()
        self.label_9.raise_()
        self.label_26.raise_()
        self.seding_ids.raise_()
        self.label_23.raise_()
        self.cmt_2.raise_()
        self.btn_clear_sending_ids.raise_()
        self.label_25.raise_()
        self.label_22.raise_()
        self.ids.raise_()
        self.label_21.raise_()
        self.btn_start_2.raise_()
        self.btn_del_2.raise_()
        self.label_10.raise_()
        self.btn_get_ids.raise_()
        self.btn_get_sending_ids.raise_()
        self.btn_get_image.raise_()
        self.btn_del_image.raise_()
        self.id_2.raise_()
        self.pwd_2.raise_()
        self.delay.raise_()
        self.send_num.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.pwd = QtWidgets.QLineEdit(self.widget)
        self.pwd.setGeometry(QtCore.QRect(70, 50, 191, 20))
        self.pwd.setObjectName("pwd")
        self.id = QtWidgets.QLineEdit(self.widget)
        self.id.setGeometry(QtCore.QRect(70, 20, 191, 20))
        self.id.setObjectName("id")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 61, 41))
        self.label_2.setObjectName("label_2")
        self.follower = QtWidgets.QLineEdit(self.widget)
        self.follower.setGeometry(QtCore.QRect(70, 310, 141, 20))
        self.follower.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.follower.setObjectName("follower")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 300, 81, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 330, 81, 41))
        self.label_4.setObjectName("label_4")
        self.count = QtWidgets.QLineEdit(self.widget)
        self.count.setGeometry(QtCore.QRect(70, 340, 171, 20))
        self.count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count.setObjectName("count")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(220, 300, 41, 41))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(240, 330, 21, 41))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.btn_add = QtWidgets.QPushButton(self.widget)
        self.btn_add.setGeometry(QtCore.QRect(470, 20, 41, 31))
        self.btn_add.setObjectName("btn_add")
        self.hashtag = QtWidgets.QLineEdit(self.widget)
        self.hashtag.setGeometry(QtCore.QRect(280, 30, 181, 20))
        self.hashtag.setObjectName("hashtag")
        self.hashtags = QtWidgets.QListWidget(self.widget)
        self.hashtags.setGeometry(QtCore.QRect(280, 60, 271, 111))
        self.hashtags.setObjectName("hashtags")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(280, 0, 91, 41))
        self.label_7.setObjectName("label_7")
        self.btn_del = QtWidgets.QPushButton(self.widget)
        self.btn_del.setGeometry(QtCore.QRect(510, 20, 41, 31))
        self.btn_del.setObjectName("btn_del")
        self.id_list = QtWidgets.QListWidget(self.widget)
        self.id_list.setGeometry(QtCore.QRect(280, 240, 271, 181))
        self.id_list.setObjectName("id_list")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(280, 210, 171, 41))
        self.label_8.setObjectName("label_8")
        self.btn_start = QtWidgets.QPushButton(self.widget)
        self.btn_start.setGeometry(QtCore.QRect(10, 370, 251, 51))
        self.btn_start.setObjectName("btn_start")
        self.btn_get_hashtags = QtWidgets.QPushButton(self.widget)
        self.btn_get_hashtags.setGeometry(QtCore.QRect(280, 180, 141, 31))
        self.btn_get_hashtags.setObjectName("btn_get_hashtags")
        self.btn_clear_hashtags = QtWidgets.QPushButton(self.widget)
        self.btn_clear_hashtags.setGeometry(QtCore.QRect(430, 180, 121, 31))
        self.btn_clear_hashtags.setObjectName("btn_clear_hashtags")
        self.btn_del_3 = QtWidgets.QPushButton(self.widget)
        self.btn_del_3.setGeometry(QtCore.QRect(220, 80, 41, 31))
        self.btn_del_3.setObjectName("btn_del_3")
        self.label_33 = QtWidgets.QLabel(self.widget)
        self.label_33.setGeometry(QtCore.QRect(10, 75, 60, 41))
        self.label_33.setObjectName("label_33")
        self.btn_get_ids_2 = QtWidgets.QPushButton(self.widget)
        self.btn_get_ids_2.setGeometry(QtCore.QRect(70, 80, 91, 31))
        self.btn_get_ids_2.setObjectName("btn_get_ids_2")
        self.btn_add_3 = QtWidgets.QPushButton(self.widget)
        self.btn_add_3.setGeometry(QtCore.QRect(170, 80, 41, 31))
        self.btn_add_3.setObjectName("btn_add_3")
        self.ids_2 = QtWidgets.QListWidget(self.widget)
        self.ids_2.setGeometry(QtCore.QRect(10, 123, 250, 176))
        self.ids_2.setObjectName("ids_2")
        self.total_num = QtWidgets.QLabel(self.widget)
        self.total_num.setGeometry(QtCore.QRect(480, 210, 61, 41))
        self.total_num.setText("")
        self.total_num.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_num.setObjectName("total_num")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(460, 210, 31, 41))
        self.label_11.setObjectName("label_11")
        self.label_7.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.btn_add.raise_()
        self.hashtags.raise_()
        self.btn_del.raise_()
        self.label_8.raise_()
        self.btn_start.raise_()
        self.btn_get_hashtags.raise_()
        self.btn_clear_hashtags.raise_()
        self.btn_del_3.raise_()
        self.label_33.raise_()
        self.btn_get_ids_2.raise_()
        self.btn_add_3.raise_()
        self.ids_2.raise_()
        self.total_num.raise_()
        self.label_11.raise_()
        self.hashtag.raise_()
        self.count.raise_()
        self.follower.raise_()
        self.id_list.raise_()
        self.pwd.raise_()
        self.id.raise_()
        self.tabWidget.addTab(self.widget, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.id_2)
        MainWindow.setTabOrder(self.id_2, self.pwd_2)
        MainWindow.setTabOrder(self.pwd_2, self.btn_get_ids)
        MainWindow.setTabOrder(self.btn_get_ids, self.btn_add_2)
        MainWindow.setTabOrder(self.btn_add_2, self.btn_del_2)
        MainWindow.setTabOrder(self.btn_del_2, self.ids)
        MainWindow.setTabOrder(self.ids, self.send_num)
        MainWindow.setTabOrder(self.send_num, self.delay)
        MainWindow.setTabOrder(self.delay, self.seding_ids)
        MainWindow.setTabOrder(self.seding_ids, self.btn_get_sending_ids)
        MainWindow.setTabOrder(self.btn_get_sending_ids, self.btn_del_sending_id)
        MainWindow.setTabOrder(self.btn_del_sending_id, self.btn_clear_sending_ids)
        MainWindow.setTabOrder(self.btn_clear_sending_ids, self.cmt_2)
        MainWindow.setTabOrder(self.cmt_2, self.img)
        MainWindow.setTabOrder(self.img, self.btn_get_image)
        MainWindow.setTabOrder(self.btn_get_image, self.btn_del_image)
        MainWindow.setTabOrder(self.btn_del_image, self.btn_start_2)
        MainWindow.setTabOrder(self.btn_start_2, self.id)
        MainWindow.setTabOrder(self.id, self.pwd)
        MainWindow.setTabOrder(self.pwd, self.btn_get_ids_2)
        MainWindow.setTabOrder(self.btn_get_ids_2, self.btn_add_3)
        MainWindow.setTabOrder(self.btn_add_3, self.btn_del_3)
        MainWindow.setTabOrder(self.btn_del_3, self.hashtag)
        MainWindow.setTabOrder(self.hashtag, self.btn_add)
        MainWindow.setTabOrder(self.btn_add, self.btn_del)
        MainWindow.setTabOrder(self.btn_del, self.hashtags)
        MainWindow.setTabOrder(self.hashtags, self.btn_get_hashtags)
        MainWindow.setTabOrder(self.btn_get_hashtags, self.btn_clear_hashtags)
        MainWindow.setTabOrder(self.btn_clear_hashtags, self.follower)
        MainWindow.setTabOrder(self.follower, self.count)
        MainWindow.setTabOrder(self.count, self.id_list)
        MainWindow.setTabOrder(self.id_list, self.btn_start)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_24.setText(_translate("MainWindow", "발송 ID"))
        self.btn_add_2.setText(_translate("MainWindow", "추가"))
        self.btn_del_sending_id.setText(_translate("MainWindow", "제거"))
        self.label_9.setText(_translate("MainWindow", "비밀번호"))
        self.label_26.setText(_translate("MainWindow", "계정 당 발송 수"))
        self.label_23.setText(_translate("MainWindow", "발송 딜레이"))
        self.btn_clear_sending_ids.setText(_translate("MainWindow", "전체제거"))
        self.label_25.setText(_translate("MainWindow", "작성원고"))
        self.label_22.setText(_translate("MainWindow", "이미지"))
        self.label_21.setText(_translate("MainWindow", "계정 정보"))
        self.btn_start_2.setText(_translate("MainWindow", "시작"))
        self.btn_del_2.setText(_translate("MainWindow", "제거"))
        self.label_10.setText(_translate("MainWindow", "아이디"))
        self.btn_get_ids.setText(_translate("MainWindow", "불러오기"))
        self.btn_get_sending_ids.setText(_translate("MainWindow", "불러오기"))
        self.btn_get_image.setText(_translate("MainWindow", "..."))
        self.btn_del_image.setText(_translate("MainWindow", "X"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "디엠 발송"))
        self.label.setText(_translate("MainWindow", "아이디"))
        self.label_2.setText(_translate("MainWindow", "비밀번호"))
        self.label_3.setText(_translate("MainWindow", "팔로워 수"))
        self.label_4.setText(_translate("MainWindow", "추출 개수"))
        self.label_5.setText(_translate("MainWindow", "명 이상"))
        self.label_6.setText(_translate("MainWindow", "개"))
        self.btn_add.setText(_translate("MainWindow", "추가"))
        self.label_7.setText(_translate("MainWindow", "해시태그 (#)"))
        self.btn_del.setText(_translate("MainWindow", "제거"))
        self.label_8.setText(_translate("MainWindow", "추출된 아이디 목록"))
        self.btn_start.setText(_translate("MainWindow", "시작"))
        self.btn_get_hashtags.setText(_translate("MainWindow", "불러오기"))
        self.btn_clear_hashtags.setText(_translate("MainWindow", "전체 삭제"))
        self.btn_del_3.setText(_translate("MainWindow", "제거"))
        self.label_33.setText(_translate("MainWindow", "계정 정보"))
        self.btn_get_ids_2.setText(_translate("MainWindow", "불러오기"))
        self.btn_add_3.setText(_translate("MainWindow", "추가"))
        self.label_11.setText(_translate("MainWindow", "총: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "아이디 추출"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())