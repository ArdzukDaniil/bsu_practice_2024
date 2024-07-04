#include <iostream>
#include "mylist.h"
#include "listiterator.h"

int main()
{
    MyList list;
    list.AddFirst(555);
    list.AddFirst(888);
    list.AddFirst(99);
    list.AddFirst(777);

    ListIterator iterator(&list);
    for (iterator.First(); !iterator.IsDone(); iterator.Next())
    {
        std::cout << iterator.CurrentItem() << '\n';
    }
    return 0;
}
