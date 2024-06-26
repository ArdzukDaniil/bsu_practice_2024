#include "mystack.h"

MyStack::MyStack() : MyList() {}
MyStack::MyStack(int value) : MyList(value) {}
MyStack::MyStack(int value1, int value2, int value3) : MyList(value1, value2, value3) {}


void MyStack::Push(int value) {
    AddFirst(value);
}


int MyStack::Pop() {
    return DeleteFirst();
}


int MyStack::Top() const {
    if (IsEmpty()) {
        return -1;
    }

    SElement* temp = first;
    return temp->data;
}

void MyStack::PrintStack() const {
    Print();
}

SElement* MyStack::GetFirst() const
{
    return first;
}
