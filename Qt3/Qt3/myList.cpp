#include "mylist.h"

MyList::MyList() {
    first = nullptr;
}

MyList::MyList(int value) {
    first = new SElement(value, nullptr);
}

MyList::MyList(int value1, int value2, int value3) {
    first = new SElement(value1, new SElement(value2, new SElement(value3, nullptr)));
}

MyList::~MyList() {
    while (first != nullptr) {
        DeleteFirst();
    }
}

bool MyList::IsEmpty() const {
    return first == nullptr;
}

void MyList::AddFirst(int value) {
    first = new SElement(value, first);
}

int MyList::DeleteFirst() {
    if (first == nullptr) {
        return -1;
    }

    SElement* temp = first;
    first = first->next;
    int value = temp->data;
    delete temp;
    return value;
}

void MyList::Print() const {
    SElement* current = first;
    while (current != nullptr) {
        std::cout << current->data << " ";
        current = current->next;
    }
    std::cout << std::endl;
}
