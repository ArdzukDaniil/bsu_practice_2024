#ifndef MYSTACK_H
#define MYSTACK_H
#include "mylist.h"

<<<<<<< HEAD
class MyStack {

=======
class MyStack 
{
>>>>>>> 3520deb372ebe7e00f1d39130abc9f753bc022aa
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
};

#endif // MYSTACK_H
