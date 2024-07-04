#include "ListIterator.h"

ListIterator::ListIterator(const MyList* aList) : _list(aList), _current(aList->GetFirst()) {}

void ListIterator::First() {
    _current = _list->GetFirst();
}

void ListIterator::Next() {
    if (_current != nullptr) {
        _current = _current->next;
    }
}

bool ListIterator::IsDone() const {
    return _current == nullptr;
}

int ListIterator::CurrentItem() const {
    return (_current != nullptr) ? _current->data : -1; 
}
