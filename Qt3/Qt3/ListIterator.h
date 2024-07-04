#pragma once

#include "mylist.h"

class ListIterator
{
public:
    ListIterator(const MyList* aList);
    void First();
    void Next();
    bool IsDone() const;
    int CurrentItem() const;

private:
    const MyList* _list;
    SElement* _current;
};