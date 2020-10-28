#include <iostream>
#include <clocale> 

using namespace std;

void getValue (double *a, double *b, char *operation)
{
    while (true) // цикл продолжается до тех пор, пока пользователь не введет корректное значение
    {
        std::cout << "Bведите выражение" <<endl;
        std::cin >> *a >> *operation >> *b;

        // Проверка на предыдущее извлечение
        if (std::cin.fail()) // если предыдущее извлечение оказалось неудачным,
        {
            std::cin.clear(); // то возвращаем cin в 'обычный' режим работы
            std::cin.ignore(32767, '\n'); // и удаляем значения предыдущего ввода из входного буфера
            std::cout << "Ввод некорректен. Попробуйте ещё раз\n";
            continue;
        }
        else
        {
            std::cin.ignore(32767, '\n'); // удаляем лишние значения

            return;
        }
    }
}
double Calculate(double a, double b, char operation)
{
    switch (operation)
    {
    case '+':
        cout << a + b;
        return true;
        break;
    case '*':
        cout << a * b;
        return true;
        break;
    case '-':
        cout << a - b;
        return true;
        break;
    case '/':
        if (b == 0)
        {
            cerr << "На 0 делить нельзя \n";
            return false;
        }
        else
        {
            cout << a / b;
            return true;
            break;
        }

    default:
        cout << "Этот оператор недопустим" << endl;
        return false;
        break;
    }
}

int main() 
{
    setlocale(LC_ALL, "Russian");

	cout << "Консольное приложение Калькулятор" << endl << endl;
	cout << "Введите операцию для выполнения. Формат: a + b | a - b | a * b | a / b " << endl;

    double a, b; char operation;
    getValue(&a, &b, &operation);

    // bool flag = 
    Calculate(a, b, operation);

}



