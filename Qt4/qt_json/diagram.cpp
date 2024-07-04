#include "diagram.h"
#include <QResizeEvent>
#include <fstream>

Diagram::Diagram(QWidget* parent) : QWidget(parent), max_value(0)
{
    pen = QPen();
}

std::istream& operator>>(std::istream& in, Diagram& diagram) {
    diagram.data.clear();
    std::string key;
    int value{};
    diagram.max_value = 0;
    while (in >> key >> value) {
        QString qKey = QString::fromStdString(key);
        diagram.data[qKey] = value;
        diagram.max_value = std::max(diagram.max_value, value);
    }
    diagram.update();
    return in;
}

void Diagram::loadData(const json& j) {
    data.clear();
    max_value = 0;
    for (auto it = j.begin(); it != j.end(); ++it) {
        QString key = QString::fromStdString(it.key());
        int value = it.value();
        data[key] = value;
        max_value = std::max(max_value, value);
    }
    update();
}

void Diagram::addData(const QString& key, int value) {
    data[key] = value;
    max_value = std::max(max_value, value);
    update();
}

void Diagram::saveData(const QString& filePath) {
    json j;
    for (const auto& [key, value] : data) {
        j[key.toStdString()] = value;
    }
    std::ofstream fout(filePath.toStdString());
    if (fout.is_open()) {
        fout << j.dump(4);
        fout.close();
    }
}

void Diagram::paintEvent(QPaintEvent* event) {
    QPainter painter(this);
    painter.begin(this);

    double diagram_width = width();
    double diagram_height = height();
    int penWidth = std::max(1, static_cast<int>(0.05 * diagram_height));

    pen.setColor(Qt::green);
    pen.setWidth(penWidth);
    painter.setPen(pen);

    double spacing = diagram_height / static_cast<double>(data.size() + 1);
    double y_pos = spacing;

    for (const auto& [key, value] : data) {
        double bar_width = (value / static_cast<double>(max_value)) * (diagram_width - 50);
        painter.drawLine(15, y_pos, 15 + bar_width, y_pos);
        y_pos += spacing;
    }

    pen.setColor(Qt::black);
    pen.setWidth(std::max(1, penWidth / 5));
    painter.setPen(pen);
    y_pos = spacing - 10;

    for (const auto& [key, value] : data) {
        double bar_width = (value / static_cast<double>(max_value)) * (diagram_width - 50);
        painter.drawText(5 + bar_width + 5, y_pos + penWidth / 2, key + ": " + QString::number(value));
        y_pos += spacing;
    }

    painter.end();
}

void Diagram::resizeEvent(QResizeEvent* event) {
    QWidget::resizeEvent(event);
    update();
}
