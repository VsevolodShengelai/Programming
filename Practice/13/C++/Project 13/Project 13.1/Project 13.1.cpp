#include <iostream>
#include <clocale> 
using namespace std;

/*
Данная программа реализует Алгоритм Эрастрофена, называемый иногда "Решетом Эрастрофена"
*/


int main()
{
    setlocale(LC_ALL, "Russian");
    int i, n;
    cout << "Введите число\n";
    cin >> n;
    bool flag;
    flag = true;
    for (i = 2; i < sqrt(n); i++)
        if (n % i == 0)
        {
            cout << "Составное";
            flag = false;
        }
    if (flag)
        cout << "Простое";
     
}