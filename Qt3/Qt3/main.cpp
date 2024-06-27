#include "mylist.h"

int main() {
    setlocale(LC_ALL, "Rus");
    MyList list(1, 2, 3);

    std::cout << "Элементы списка: ";
    for (MyList::Iterator it = list.begin(); it != list.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;

    return 0;
}
