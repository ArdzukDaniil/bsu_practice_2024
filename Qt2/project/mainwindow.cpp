#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setFixedSize(size());
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButtonPush_clicked()
{
    bool ok;
    int value = ui->lineEdit->text().toInt(&ok);
    if (ok) {
        stack.Push(value);
        updateStackView();
    }
}

void MainWindow::on_pushButtonPop_clicked()
{
    if (!stack.IsEmpty()) {
        stack.Pop();
        updateStackView();
    }
}

void MainWindow::on_pushButtonTop_clicked()
{
    if (!stack.IsEmpty()) {
        int topValue = stack.Top();
        ui->labelTopValue->setText(QString::number(topValue));
    }
}

void MainWindow::updateStackView()
{
    ui->listWidgetStack->clear();
    SElement* current = stack.GetFirst();
    while (current != nullptr) {
        ui->listWidgetStack->addItem(QString::number(current->data));
        current = current->next;
    }
}
