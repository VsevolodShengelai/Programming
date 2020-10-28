// CalculatorFinal.cpp : Defines the entry point for the console application.
   //

#include "stdafx.h"       // Including header
#include <iostream>       // Including ioStream
using namespace std;      // Namespace

void calc(double x, double y);
double result;
double n1, n2;             // Declaring Variables
char q, operation;


int main()
{
    cout << "Welcome to My Calculator" << endl; // Outputs welcome message
    cout << "" << endl;                               // Blank Space
    cout << "INSTRUCTIONS: Input a mathmatical equation" << endl; // Outputs instruction            
    cout << "              EX: 2 + 2" << endl;       // Outputs instruction
    cout << "" << endl;                               // Blank Space
    cout << "Operators:" << endl;                     // Outputs operation header
    cout << "For Addition, select '+'" << endl;        // Outputs ADD instruction
    cout << "For Subtraction, select '-'" << endl;    // Outputs SUB instruction
    cout << "For Multiplication, select '*'" << endl; // Outputs MUL instruction
    cout << "For Division, select '/'" << endl;       // Outputs DIV instruction
    cout << "" << endl;                               // Blank Space
    cout << "To clear, select 'c'" << endl;  // Outputs clear instruction
    cout << "To quit, select 'q'" << endl;   // Outputs QUIT instruction
    cout << "" << endl;                                                                  // Blank Space
    cout << "Input a mathmatical equation" << endl;                                      // Input instructions
    cin >> n1 >> operation >> n2;
calc:(n1, n2);
    cout << "The answer is:" << result << endl;
    std::cin >> q;             // Input "q" to "quit"
    return 0;
}

void calc(double x, double y)                                                       // Operator function
{
    x = n1;
    y = n2;

    switch (operation)                                                           // Operator swtich statement
    {
    case '+':
        result = x + y;
        break;

    case '-':
        result = x - y;
        break;

    case '*':
        result = x * y;
        break;

    case '/':
        result = x / y;
        break;

    default:
        cout << "Improper equation. Please input a valid mathmatical equation" << endl;
        cin >> n1 >> operation >> n2;
        calc(n1, n2);
    }

}