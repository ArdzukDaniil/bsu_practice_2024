#pragma once

#include <iostream>

struct SElement {
    int data;
    SElement* next;
    SElement(int data_, SElement* next_) : data{ data_ }, next{ next_ } {};
};

class MyList {
private:
    SElement* first;

public:
    MyList();
    MyList(int val);
    MyList(int val1, int val2, int val3);
    ~MyList();

    bool IsEmpty() const;
    void AddFirst(int value);
    int DeleteFirst();
    void Print() const;

    class Iterator {
    private:
        SElement* current;

    public:
        Iterator(SElement* element) : current{ element } {}

        Iterator& operator++() {
            current = current->next;
            return *this;
        }

        int operator*() const {
            return current->data;
        }

        bool operator!=(const Iterator& other) const {
            return current != other.current;
        }
    };

    Iterator begin() {
        return Iterator(first);
    }

    Iterator end() {
        return Iterator(nullptr);
    }
};

