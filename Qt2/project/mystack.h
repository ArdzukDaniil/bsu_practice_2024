#ifndef MYSTACK_H
#define MYSTACK_H
#include "mylist.h"
#include <iostream>
#include <vector>

class MyStack {
private:
    MyList* list;
public:
    MyStack();
    MyStack(int value);
    MyStack(int value1, int value2, int value3);
    ~MyStack();

    void Push(int value);
    int Pop();
    int Top() const;
    void PrintStack() const;
    bool IsEmpty() const;
    SElement* GetFirst() const;
    std::vector<int> ToVector() const;
};

#endif // MYSTACK_H
