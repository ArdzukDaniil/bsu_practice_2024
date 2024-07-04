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

bool MyList::Empty() const {
    return first == nullptr;
}

void MyList::AddFirst(int value) {
    first = new SElement(value, first);
}

void MyList::Print() const {
    SElement* current = first;
    while (current != nullptr) {
        std::cout << current->data << " ";
        current = current->next;
    }
    std::cout << std::endl;
}

int MyList::Count() const {
    int count = 0;
    SElement* current = first;
    while (current != nullptr) {
        count++;
        current = current->next;
    }
    return count;
}

int MyList::Get(int n) const {
    if (n < 0) return -1;

    SElement* current = first;
    for (int i = 0; current != nullptr && i < n; i++) {
        current = current->next;
    }
    return (current != nullptr) ? current->data : -1;
}

void MyList::ToVector(std::vector<int>& Vec) const {
    Vec.clear();
    SElement* current = first;
    while (current != nullptr) {
        Vec.push_back(current->data);
        current = current->next;
    }
}

SElement* MyList::GetFirst() const {
    return first;
}
