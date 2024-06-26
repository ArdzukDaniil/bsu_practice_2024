/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QListWidget *listWidgetStack;
    QLabel *labelTopValue;
    QPushButton *pushButtonTop;
    QPushButton *pushButtonPop;
    QPushButton *pushButtonPush;
    QLineEdit *lineEdit;
    QLabel *label;
    QLabel *label_2;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(398, 350);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        listWidgetStack = new QListWidget(centralwidget);
        listWidgetStack->setObjectName(QString::fromUtf8("listWidgetStack"));
        listWidgetStack->setGeometry(QRect(30, 20, 151, 261));
        labelTopValue = new QLabel(centralwidget);
        labelTopValue->setObjectName(QString::fromUtf8("labelTopValue"));
        labelTopValue->setGeometry(QRect(210, 210, 141, 31));
        pushButtonTop = new QPushButton(centralwidget);
        pushButtonTop->setObjectName(QString::fromUtf8("pushButtonTop"));
        pushButtonTop->setGeometry(QRect(200, 240, 171, 29));
        pushButtonPop = new QPushButton(centralwidget);
        pushButtonPop->setObjectName(QString::fromUtf8("pushButtonPop"));
        pushButtonPop->setGeometry(QRect(200, 150, 171, 29));
        pushButtonPop->setIconSize(QSize(25, 20));
        pushButtonPush = new QPushButton(centralwidget);
        pushButtonPush->setObjectName(QString::fromUtf8("pushButtonPush"));
        pushButtonPush->setGeometry(QRect(200, 110, 171, 29));
        lineEdit = new QLineEdit(centralwidget);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setGeometry(QRect(200, 60, 171, 41));
        label = new QLabel(centralwidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(200, 20, 181, 41));
        label_2 = new QLabel(centralwidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(200, 190, 141, 20));
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 398, 25));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        labelTopValue->setText(QString());
        pushButtonTop->setText(QCoreApplication::translate("MainWindow", "Top", nullptr));
        pushButtonPop->setText(QCoreApplication::translate("MainWindow", "Pop", nullptr));
        pushButtonPush->setText(QCoreApplication::translate("MainWindow", "Push", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p>\320\222\320\262\320\265\320\264\320\270\321\202\320\265 \320\267\320\275\320\260\321\207\320\265\320\275\320\270\320\265,<br/> \320\272\320\276\321\202\320\276\321\200\320\276\320\265 \321\205\320\276\321\202\320\270\321\202\320\265 \320\264\320\276\320\261\320\260\320\262\320\270\321\202\321\214</p></body></html>", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "\320\222\320\265\321\200\321\210\320\270\320\275\320\260 \321\201\321\202\320\265\320\272\320\260: ", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
