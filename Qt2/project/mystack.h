#ifndef MYSTACK_H
#define MYSTACK_H
#include "mylist.h"

class MyStack: public MyList
{
public:
    MyStack();
    MyStack(int value);
    MyStack(int value1, int value2, int value3);
    void Push(int value);
    int Pop();
    int Top() const;
    void PrintStack() const;

     SElement* GetFirst() const;
};

#endif // MYSTACK_H
