# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/user/git/goxgui/goxgui/ui/preferences.ui'
#
# Created: Mon May  6 18:34:36 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName(_fromUtf8("Preferences"))
        Preferences.resize(740, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Preferences.sizePolicy().hasHeightForWidth())
        Preferences.setSizePolicy(sizePolicy)
        Preferences.setMinimumSize(QtCore.QSize(740, 400))
        Preferences.setMaximumSize(QtCore.QSize(740, 400))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Preferences)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(Preferences)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabAuth = QtGui.QWidget()
        self.tabAuth.setObjectName(_fromUtf8("tabAuth"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabAuth)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBoxMarket = QtGui.QGroupBox(self.tabAuth)
        self.groupBoxMarket.setEnabled(False)
        self.groupBoxMarket.setFlat(True)
        self.groupBoxMarket.setObjectName(_fromUtf8("groupBoxMarket"))
        self.gridLayout = QtGui.QGridLayout(self.groupBoxMarket)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEditPassword = QtGui.QLineEdit(self.groupBoxMarket)
        self.lineEditPassword.setEnabled(False)
        self.lineEditPassword.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.lineEditPassword.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.lineEditPassword.setObjectName(_fromUtf8("lineEditPassword"))
        self.gridLayout.addWidget(self.lineEditPassword, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBoxMarket)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.labelPassword = QtGui.QLabel(self.groupBoxMarket)
        self.labelPassword.setWordWrap(True)
        self.labelPassword.setObjectName(_fromUtf8("labelPassword"))
        self.gridLayout.addWidget(self.labelPassword, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBoxMarket)
        self.groupBoxApplication = QtGui.QGroupBox(self.tabAuth)
        self.groupBoxApplication.setFlat(True)
        self.groupBoxApplication.setObjectName(_fromUtf8("groupBoxApplication"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxApplication)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBoxApplication)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBoxApplication)
        self.label_4.setMinimumSize(QtCore.QSize(100, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEditSecret = QtGui.QLineEdit(self.groupBoxApplication)
        self.lineEditSecret.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.lineEditSecret.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.lineEditSecret.setObjectName(_fromUtf8("lineEditSecret"))
        self.gridLayout_2.addWidget(self.lineEditSecret, 3, 1, 1, 1)
        self.lineEditKey = QtGui.QLineEdit(self.groupBoxApplication)
        self.lineEditKey.setObjectName(_fromUtf8("lineEditKey"))
        self.gridLayout_2.addWidget(self.lineEditKey, 2, 1, 1, 1)
        self.labelKeySecret = QtGui.QLabel(self.groupBoxApplication)
        self.labelKeySecret.setWordWrap(True)
        self.labelKeySecret.setObjectName(_fromUtf8("labelKeySecret"))
        self.gridLayout_2.addWidget(self.labelKeySecret, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBoxApplication)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.tabWidget.addTab(self.tabAuth, _fromUtf8(""))
        self.tabVarious = QtGui.QWidget()
        self.tabVarious.setObjectName(_fromUtf8("tabVarious"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tabVarious)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBoxCurrency = QtGui.QGroupBox(self.tabVarious)
        self.groupBoxCurrency.setEnabled(True)
        self.groupBoxCurrency.setFlat(True)
        self.groupBoxCurrency.setObjectName(_fromUtf8("groupBoxCurrency"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBoxCurrency)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.comboBoxCurrency = QtGui.QComboBox(self.groupBoxCurrency)
        self.comboBoxCurrency.setObjectName(_fromUtf8("comboBoxCurrency"))
        self.gridLayout_3.addWidget(self.comboBoxCurrency, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBoxCurrency)
        self.label_6.setMinimumSize(QtCore.QSize(100, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 2, 1, 1)
        self.labelCurrency = QtGui.QLabel(self.groupBoxCurrency)
        self.labelCurrency.setTextFormat(QtCore.Qt.AutoText)
        self.labelCurrency.setWordWrap(True)
        self.labelCurrency.setObjectName(_fromUtf8("labelCurrency"))
        self.gridLayout_3.addWidget(self.labelCurrency, 0, 1, 1, 2)
        self.verticalLayout_5.addWidget(self.groupBoxCurrency)
        spacerItem2 = QtGui.QSpacerItem(20, 164, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.verticalLayout_5.setStretch(1, 1)
        self.tabWidget.addTab(self.tabVarious, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelStatus = QtGui.QLabel(Preferences)
        self.labelStatus.setText(_fromUtf8(""))
        self.labelStatus.setObjectName(_fromUtf8("labelStatus"))
        self.horizontalLayout.addWidget(self.labelStatus)
        self.buttonBox = QtGui.QDialogButtonBox(Preferences)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Preferences)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Preferences.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Preferences.reject)
        QtCore.QMetaObject.connectSlotsByName(Preferences)
        Preferences.setTabOrder(self.lineEditPassword, self.lineEditKey)
        Preferences.setTabOrder(self.lineEditKey, self.lineEditSecret)
        Preferences.setTabOrder(self.lineEditSecret, self.buttonBox)
        Preferences.setTabOrder(self.buttonBox, self.tabWidget)
        Preferences.setTabOrder(self.tabWidget, self.comboBoxCurrency)

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(QtGui.QApplication.translate("Preferences", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxMarket.setTitle(QtGui.QApplication.translate("Preferences", "Application", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditPassword.setToolTip(QtGui.QApplication.translate("Preferences", "Application password", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditPassword.setPlaceholderText(QtGui.QApplication.translate("Preferences", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Preferences", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPassword.setText(QtGui.QApplication.translate("Preferences", "Set an application-wide password to protect account-related functionalities against misuse.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxApplication.setTitle(QtGui.QApplication.translate("Preferences", "Market", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Preferences", "Key:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Preferences", "Secret:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditSecret.setToolTip(QtGui.QApplication.translate("Preferences", "Insert your MtGox secret here", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditSecret.setPlaceholderText(QtGui.QApplication.translate("Preferences", "Secret", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditKey.setToolTip(QtGui.QApplication.translate("Preferences", "Insert your MtGox key here", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditKey.setPlaceholderText(QtGui.QApplication.translate("Preferences", "Key", None, QtGui.QApplication.UnicodeUTF8))
        self.labelKeySecret.setText(QtGui.QApplication.translate("Preferences", "Insert your market\'s (e.g. MtGox) API key here. If you don\'t have an API key yet, you should be able to generate one on your market\'s website.", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAuth), QtGui.QApplication.translate("Preferences", "Authentification", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxCurrency.setTitle(QtGui.QApplication.translate("Preferences", "Currency", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Preferences", "Fiat:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCurrency.setText(QtGui.QApplication.translate("Preferences", "Select the fiat currency you would like to trade", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVarious), QtGui.QApplication.translate("Preferences", "Various Settings", None, QtGui.QApplication.UnicodeUTF8))

