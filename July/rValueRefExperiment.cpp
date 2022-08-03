#include <iostream>

using std::cout;

void func(int &lval)
{
    cout<<"lvalue call\n";
}

void func(int &&rval)
{
    cout<<"rvalue call\n";
}

template<typename T>
void Wrapper(T&& universal)
{
    /* rvalue references are themselves lvalues. While this might seem confusing at first glance, 
    it really is the mechanism that enables move semantics: 
    A reference is always defined in a certain context (such as in the above example the variable universal).
    Even though the object it refers to (the number 5) may be disposable in the context it has been 
    created (the main function), it is not disposable in the context of the reference . 
    So within the scope of Wrapper, universal is an lvalue as it gives access to the memory location 
    where the number 5 is stored. */

    func(universal);
}

int main()
{
    int lval = 5;
    //Wrapper(lval);
    Wrapper(10);
    func(10);
    return 0;
}

template<typename T>
void magicFunction(T&& param);
magicFunction<int>(10); // rvalue
int val = 20;
magicFunction<int>(val); //lvalue