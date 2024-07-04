#ifndef DIAGRAM_H
#define DIAGRAM_H

#include <QWidget>
#include <QPen>
#include <QColor>
#include <QPainter>
#include <QPoint>
#include <iostream>
#include <map>
#include "json.hpp"

class Diagram : public QWidget
{
    Q_OBJECT
public:
    using json = nlohmann::json;
    Diagram(QWidget* parent = nullptr);

    friend std::istream& operator>>(std::istream&, Diagram&);

    void loadData(const json& j);
    void addData(const QString& key, int value);
    void saveData(const QString& filePath);

protected:
    void paintEvent(QPaintEvent*) override;
    void resizeEvent(QResizeEvent* event) override;

private:
    std::map<QString, int> data;
    int max_value;
    QPen pen;
};

#endif // DIAGRAM_H
