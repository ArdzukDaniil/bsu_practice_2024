#pragma once
#include <iostream>
#include <vector>

struct SElement
{
    int data;
    SElement* next;
    SElement(int data_, SElement* next_) :data{ data_ }, next{ next_ } {};
};

class MyList
{
protected:
    SElement* first;
public:
    MyList();
    MyList(int val);
    MyList(int val1, int val2, int val3);
    ~MyList();

    bool Empty() const; 
    void AddFirst(int Value);
    int DeleteFirst();
    void Print()const;

    int Count() const; 
    int Get(int n) const; 
    void ToVector(std::vector<int>& Vec) const;

    SElement* GetFirst() const;
};