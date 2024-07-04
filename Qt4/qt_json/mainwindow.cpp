#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QInputDialog>
#include <QMessageBox>
#include <fstream>
#include "diagram.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    connect(ui->openDiagramButton, &QPushButton::clicked, this, &MainWindow::onOpenDiagramClick);
    connect(ui->addDataButton, &QPushButton::clicked, this, &MainWindow::onAddDataClick);
    connect(ui->saveDiagramButton, &QPushButton::clicked, this, &MainWindow::onSaveDiagramClick);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::onOpenDiagramClick() {
    QString file_path = QFileDialog::getOpenFileName(this, tr("Open Diagram"), "", tr("JSON Files (*.json)"));
    if (!file_path.isEmpty()) {
        std::ifstream fin(file_path.toStdString());
        if (fin) {
            nlohmann::json json;
            fin >> json;
            fin.close();
            ui->diagram->loadData(json);
    }
}

void MainWindow::onAddDataClick() {
    bool ok;
    QString key = QInputDialog::getText(this, tr("Add Data"), tr("Key:"), QLineEdit::Normal, "", &ok);
    if (!ok || key.isEmpty()) return;
    int value = QInputDialog::getInt(this, tr("Add Data"), tr("Value:"), 0, 0, 100, 1, &ok);
    if (ok) {
        ui->diagram->addData(key, value);
    }
}

void MainWindow::onSaveDiagramClick() {
    QString file_path = QFileDialog::getSaveFileName(this, tr("Save Diagram"), "", tr("JSON Files (*.json)"));
    if (!file_path.isEmpty()) {
        ui->diagram->saveData(file_path);
    }
}
