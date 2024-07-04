#include "mystack.h"

MyStack::MyStack() {
    list = new MyList();
}

MyStack::MyStack(int value) {
    list = new MyList(value);
}

MyStack::MyStack(int value1, int value2, int value3) {
    list = new MyList(value1, value2, value3);
}

MyStack::~MyStack() {
    delete list;
}

void MyStack::Push(int value) {
    list->AddFirst(value);
}

int MyStack::Pop() {
    return list->DeleteFirst();
}

int MyStack::Top() const {
    if (list->IsEmpty()) {
        return -1;
    }
    return list->GetFirst()->data;
}

bool MyStack::IsEmpty() const {
    return list->IsEmpty();
}

void MyStack::PrintStack() const {
    list->Print();
}

SElement* MyStack::GetFirst() const {
    return list->GetFirst();
}

std::vector<int> MyStack::ToVector() const {
    return list->ToVector();
}
