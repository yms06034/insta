# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_id.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 440)
        MainWindow.setMinimumSize(QtCore.QSize(581, 440))
        MainWindow.setMaximumSize(QtCore.QSize(581, 440))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.count = QtWidgets.QLineEdit(self.centralwidget)
        self.count.setGeometry(QtCore.QRect(80, 340, 171, 20))
        self.count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count.setObjectName("count")
        self.hashtag = QtWidgets.QLineEdit(self.centralwidget)
        self.hashtag.setGeometry(QtCore.QRect(290, 30, 181, 20))
        self.hashtag.setObjectName("hashtag")
        self.hashtags = QtWidgets.QListWidget(self.centralwidget)
        self.hashtags.setGeometry(QtCore.QRect(290, 60, 271, 111))
        self.hashtags.setObjectName("hashtags")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 330, 81, 41))
        self.label_4.setObjectName("label_4")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(20, 370, 251, 51))
        self.btn_start.setObjectName("btn_start")
        self.btn_clear_hashtags = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear_hashtags.setGeometry(QtCore.QRect(440, 180, 121, 31))
        self.btn_clear_hashtags.setObjectName("btn_clear_hashtags")
        self.ids_2 = QtWidgets.QListWidget(self.centralwidget)
        self.ids_2.setGeometry(QtCore.QRect(20, 123, 250, 176))
        self.ids_2.setObjectName("ids_2")
        self.btn_get_ids_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_get_ids_2.setGeometry(QtCore.QRect(80, 80, 91, 31))
        self.btn_get_ids_2.setObjectName("btn_get_ids_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 210, 171, 41))
        self.label_8.setObjectName("label_8")
        self.btn_del = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del.setGeometry(QtCore.QRect(520, 20, 41, 31))
        self.btn_del.setObjectName("btn_del")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(470, 210, 31, 41))
        self.label_11.setObjectName("label_11")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 330, 21, 41))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.total_num = QtWidgets.QLabel(self.centralwidget)
        self.total_num.setGeometry(QtCore.QRect(490, 210, 61, 41))
        self.total_num.setText("")
        self.total_num.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_num.setObjectName("total_num")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(480, 20, 41, 31))
        self.btn_add.setObjectName("btn_add")
        self.pwd = QtWidgets.QLineEdit(self.centralwidget)
        self.pwd.setGeometry(QtCore.QRect(80, 50, 191, 20))
        self.pwd.setObjectName("pwd")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 0, 91, 41))
        self.label_7.setObjectName("label_7")
        self.follower = QtWidgets.QLineEdit(self.centralwidget)
        self.follower.setGeometry(QtCore.QRect(80, 310, 141, 20))
        self.follower.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.follower.setObjectName("follower")
        self.id_list = QtWidgets.QListWidget(self.centralwidget)
        self.id_list.setGeometry(QtCore.QRect(290, 240, 271, 181))
        self.id_list.setObjectName("id_list")
        self.btn_del_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del_3.setGeometry(QtCore.QRect(230, 80, 41, 31))
        self.btn_del_3.setObjectName("btn_del_3")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(20, 75, 60, 41))
        self.label_33.setObjectName("label_33")
        self.id = QtWidgets.QLineEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(80, 20, 191, 20))
        self.id.setObjectName("id")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 61, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 61, 41))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 300, 41, 41))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 300, 81, 41))
        self.label_3.setObjectName("label_3")
        self.btn_get_hashtags = QtWidgets.QPushButton(self.centralwidget)
        self.btn_get_hashtags.setGeometry(QtCore.QRect(290, 180, 141, 31))
        self.btn_get_hashtags.setObjectName("btn_get_hashtags")
        self.btn_add_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_3.setGeometry(QtCore.QRect(180, 80, 41, 31))
        self.btn_add_3.setObjectName("btn_add_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "추출 개수"))
        self.btn_start.setText(_translate("MainWindow", "시작"))
        self.btn_clear_hashtags.setText(_translate("MainWindow", "전체 삭제"))
        self.btn_get_ids_2.setText(_translate("MainWindow", "불러오기"))
        self.label_8.setText(_translate("MainWindow", "추출된 아이디 목록"))
        self.btn_del.setText(_translate("MainWindow", "제거"))
        self.label_11.setText(_translate("MainWindow", "총: "))
        self.label_6.setText(_translate("MainWindow", "개"))
        self.btn_add.setText(_translate("MainWindow", "추가"))
        self.label_7.setText(_translate("MainWindow", "해시태그 (#)"))
        self.btn_del_3.setText(_translate("MainWindow", "제거"))
        self.label_33.setText(_translate("MainWindow", "계정 정보"))
        self.label.setText(_translate("MainWindow", "아이디"))
        self.label_2.setText(_translate("MainWindow", "비밀번호"))
        self.label_5.setText(_translate("MainWindow", "명 이상"))
        self.label_3.setText(_translate("MainWindow", "팔로워 수"))
        self.btn_get_hashtags.setText(_translate("MainWindow", "불러오기"))
        self.btn_add_3.setText(_translate("MainWindow", "추가"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
