from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from utils import *
from icons import icons

activeLoginWindows = []

class Ui_MainWindow(object):
    def setupUi(self, mode, MainWindow):
        self.mode = mode
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 3, 1, 1)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 2, 1, 1)
        spacerItem3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        self.LoginForm = QWidget(self.centralwidget)
        self.LoginForm.setStyleSheet("#LoginForm {\n"
            "    border: 1px solid;\n"
            "    border-radius: 3px;\n"
            "}")
        self.LoginForm.setObjectName("LoginForm")
        self.formLayout = QFormLayout(self.LoginForm)
        self.formLayout.setContentsMargins(16, 16, 16, 16)
        self.formLayout.setSpacing(16)
        self.formLayout.setObjectName("formLayout")
        self.usernameLabel = QLabel(self.LoginForm)
        font = QFont()
        font.setPointSize(12)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.usernameLabel)
        self.usernameLineEdit = QLineEdit(self.LoginForm)
        font = QFont()
        font.setPointSize(12)
        self.usernameLineEdit.setFont(font)
        self.usernameLineEdit.setText("")
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.usernameLineEdit)
        self.passwordLabel = QLabel(self.LoginForm)
        font = QFont()
        font.setPointSize(12)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.passwordLabel)
        self.passwordLineEdit = QLineEdit(self.LoginForm)
        self.passwordLineEdit.setEnabled(True)
        font = QFont()
        font.setPointSize(12)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setText("")
        self.passwordLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.passwordLineEdit)
        self.pushButton = QPushButton(self.LoginForm)
        font = QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.pushButton)
        self.gridLayout_2.addWidget(self.LoginForm, 1, 1, 1, 2)
        spacerItem4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 1, 1, 1)
        spacerItem5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 770, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(lambda: (MainWindow.close(), addUser(self.mode, self.usernameLineEdit.text(), self.passwordLineEdit.text())))


    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))


def ActionUserAdd(mode, menu):
    class CustomMainWindow(QMainWindow):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            activeLoginWindows.append(self)

        def closeEvent(self, event):
            activeLoginWindows.remove(self)
            event.accept()


    ui = Ui_MainWindow()
    MainWindow = CustomMainWindow()
    ui.setupUi(mode, MainWindow)
    MainWindow.show()


def updateUserRemoveMenu(mode, menu):
    users = getUsersInfo()

    menu.clear()
    for user in users[mode]:
        icon = icons['active'] if user['active'] else icons['inactive']
        submenu = menu.addMenu(icon, user['username'])
        subaction = submenu.addAction(icons['confirm'], '&Confirm')
        subaction.triggered.connect(lambda id=user['id']: deleteUser(mode, id))


def updateUserViewMenu(mode, menu):
    users = getUsersInfo()

    menu.clear()
    for user in users[mode]:
        if user['active']:
            submenu = menu.addMenu(icons['active'], user['username'])
            subaction = submenu.addAction(icons['confirm'], '&Confirm')
            subaction.triggered.connect(lambda *_, user=user: deactivateUser(mode, user.get('id')))

        else:
            subaction = menu.addAction(icons['inactive'], user['username'])
            subaction.triggered.connect(lambda *_, user=user: activateUser(mode, user.get('id')))
        
    
def updateMainMenu(app, menu):
    menu.clear()

    appData = getAppInfo()

    if appData['active']:
        subaction = menu.addAction(icons['active'], 'Active Monitoring')
        subaction.triggered.connect(lambda: deactivateMonitoring())

    else:
        subaction = menu.addAction(icons['inactive'], 'Inactive Monitoring')
        subaction.triggered.connect(lambda: activateMonitoring())

    menu.addSeparator()

    disabled = not appData['active']

    submenu = menu.addMenu(icons['add'], 'Add Account')
    submenu.addAction(icons['email'], 'Email').triggered.connect(lambda menu=submenu: ActionUserAdd('email', menu))
    submenu.setDisabled(disabled)

    submenu = menu.addMenu(icons['remove'], 'Remove Account')
    submenu.addMenu(icons['email'], 'Email').aboutToShow.connect(lambda menu=submenu: updateUserRemoveMenu('email', menu))
    submenu.setDisabled(disabled)

    submenu = menu.addMenu(icons['view'], 'View Accounts')
    submenu.addMenu(icons['email'], 'Email').aboutToShow.connect(lambda menu=submenu: updateUserViewMenu('email', menu))
    submenu.setDisabled(disabled)

    menu.addSeparator()
    subaction = menu.addAction(icons['quit'], '&Quit')
    subaction.triggered.connect(app.quit)



def main():
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)

    systray = QSystemTrayIcon()
    systray.setIcon(icons['main'])
    systray.setVisible(True)

    menu = QMenu('PAIN')
    menu.aboutToShow.connect(lambda: updateMainMenu(app, menu))
    systray.setContextMenu(menu)
    app.exec_()


if __name__ == '__main__':
    main()
