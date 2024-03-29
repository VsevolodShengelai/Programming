﻿// Project 9.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <clocale>
#include <cmath>

using namespace std;
bool Proverka(int *h, int *m, int *min)
{
	if (*h >= 0 && *h <= 23 && *m >= 0 && *m <= 59)
	{
		*min = 60 * (*h) + (*m);
		return true;
	}
	else
	{
		cout << "Вы ввели неверное значение времени. Повторите ввод, пожалуйста \n";
		return false;
	}
		
}

int main()
{
	
	setlocale(LC_ALL, "Russian");
	cout << "Программа \'Встреча\' \n";
	cout << "Введите два значения времени в виде часов и минут в формате ЧЧ:ММ \n";
	char s;
	int h1, h2, m1, m2, min1, min2;
	min1, min2 = 0;
	while (true)
	{
        cin >> h1 >> s >> m1;
		bool rez = Proverka(&h1, &m1, &min1);
		if (rez == 1)
			break;
	}

	while (true)
	{
		cin >> h2 >> s >> m2;
		bool rez = Proverka(&h2, &m2, &min2);
		if (rez == 1)
			break;
	}

	if (abs(min2 - min1) <= 15)
		cout << "Встреча состоится";
	else
		cout << "Встреча не состоится";
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
