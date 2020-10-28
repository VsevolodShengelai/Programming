// Project 7.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <clocale>
#include <math.h>
#include <cmath>

double getValue_mode1()
{
    while (true) //Цикл продолжается до тех пор, пока пользователь не введёт корректное значение
    {
        double a;
        std::cin >> a;
        
        if (std::cin.fail())  //Если предыдущее значене вызвало режим отказа, то все последующие запросы на извлечение данных будут проигнорированы
        {
            std::cin.clear();  //то возвращаем сin в обычный режим работы
            std::cin.ignore(32767, '\n');  //Удаляем определЁнное кол-во символов из буфера обмена влоть до \n (который также удаляется)
        }
        else //Если всё хорошо, возвращаем a
        {
            std::cin.ignore(32767, '\n'); //Удалив лишние значения

            return a;
        }

    }
}

void getValue_mode2(double *px, double *py) 
{

    while (true)
    {

        std::cin >> (*px) >> (*py);
        if (std::cin.fail())
        {
            std::cin.clear();
            std::cin.ignore(32767, '\n');
            std::cout << "Введите значения двух координат через пробел\n";
            continue;
        }
        //else if (double(*px) && double(*py))
        //{
            std::cin.ignore(32767, '\n');
            
            return;
        //}
        //else
            // std::cout << "Введите значения двух координат через пробел\n";
    }
}

int getMode()
{
    while (true)
    {
        int mode;
        std::cin >> mode;

        std::cin.ignore(32767, '\n');

        if (std::cin.fail())
        {
            std::cin.clear();
            std::cin.ignore(32767, '\n');
            std::cout << "Неверный ввод. Введите \"1\" или \"2\"\n";
        }
        else if (mode == 1 || mode == 2)
            return mode;
        else
            std::cout << "Неверный ввод. Введите \"1\" или \"2\"\n";
    }
}

double teoremaGerona(double a, double b, double c)
{
    if ((a + b) <= c || (a + c) <= b || (c + b) <= a)
    {
        std::cout << "Треугольник не существует\n";
        bool flag = true;
        return flag;
    }

    double p = (a + b + c) / 2;
    double S = p * (p - a) * (p - b) * (p - c);
    S = sqrt(S);
    std::cout << "S = " << S;
    bool flag = false;
    return flag;
}


int main()
{
    setlocale(LC_ALL, "Russian");
    std::cout << "Выберите способ нахождения площади треугольника (\"1\" или \"2\")" <<"\n";
    std::cout << "\"1\" - через длины сторон" << "\n";
    std::cout << "\"2\" - через координаты вершин" << "\n";
    std::cout << "Затем введите требуемые значения" << "\n\n";
    int mode = getMode();
    
    while (true) 
    {
        if (mode == 1)
        {
            double a, b, c;
            a = getValue_mode1();
            b = getValue_mode1();
            c = getValue_mode1();

            bool flag = teoremaGerona(a, b, c);
            if (flag == true) continue;
            else break;
        }
        else if (mode == 2)
        {
            double x1, y1, x2, y2, x3, y3;
            getValue_mode2(&x1, &y1);
            getValue_mode2(&x2, &y2);
            getValue_mode2(&x3, &y3);

            double a, b, c;
            
            a = sqrt((pow((x1 - x2), 2) + pow((y1 - y2), 2)));
            b = sqrt((pow((x1 - x3), 2) + pow((y1 - y3), 2)));
            c = sqrt((pow((x2 - x3), 2) + pow((y2 - y3), 2)));

            bool flag = teoremaGerona(a, b, c);
            if (flag == true) continue;
            else break;
        }

    }
}



// Запуск программы: CTRL+F5 или меню "Отладка" > "Запуск без отладки"
// Отладка программы: F5 или меню "Отладка" > "Запустить отладку"

// Советы по началу работы 
//   1. В окне обозревателя решений можно добавлять файлы и управлять ими.
//   2. В окне Team Explorer можно подключиться к системе управления версиями.
//   3. В окне "Выходные данные" можно просматривать выходные данные сборки и другие сообщения.
//   4. В окне "Список ошибок" можно просматривать ошибки.
//   5. Последовательно выберите пункты меню "Проект" > "Добавить новый элемент", чтобы создать файлы кода, или "Проект" > "Добавить существующий элемент", чтобы добавить в проект существующие файлы кода.
//   6. Чтобы снова открыть этот проект позже, выберите пункты меню "Файл" > "Открыть" > "Проект" и выберите SLN-файл.
