#ifndef MYLIST_H
#define MYLIST_H
#include <iostream>

struct SElement
{
    int data;
    SElement* next;
    SElement(int data_, SElement* next_) :data{ data_ }, next{ next_ } {};
};
class MyList
{
protected:
    SElement *first;
public:
    MyList();
    MyList(int val);
    MyList(int val1, int val2, int val3);
    ~MyList();

    bool IsEmpty() const;
    void AddFirst(int Value);
    int DeleteFirst();
    void Print()const;

    SElement* GetFirst() const;
};

#endif // MYLIST_H
