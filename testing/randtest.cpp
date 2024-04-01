#include <random>
#include <iostream>


int main()
{
    for(int i = 0; i < 100; i++)
    {
        int n = std::rand()%1000;
        std::cout << n << '\n';
    }
    return 0;
}