#include <iostream>
#include "the_first.h"
#include "the_second.h"
#include "the_third.h"
#include <iomanip>
#define PI 3.14159265358979323846

int main()
{
    //std::cout << "Hello World!\n";
    //std::cout << fact(4);
    std::cout << "n""\t""n!" << std::endl;
    for (int i = 1; i <= 10; i++)
    {
        std::cout << i << "\t" << fact(i) <<std::endl;
    }

    std::cout << std::endl;

    std::cout << "x""\t""sin(x)" << std::endl;
    double x = 0;
    for (double x = 0; x <= PI / 4; x = x + (PI / 180))
    {
        std::cout << x << "\t" << std:: setprecision(4) << Tailor(x , 5) << std::endl;
        ;
    }

    std::cout << std::endl;

    std::cout << "k""\t""C(k, 10)" << std::endl;
    int n = 10;
    for (int i = 1; i <= 10; i++)
    {
        std::cout << i << "\t" << Soch(i, 10) << std::endl;
    }

    std::cout << std::endl;
}

