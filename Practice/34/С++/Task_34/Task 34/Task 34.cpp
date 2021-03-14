#include <iostream>

using namespace std;

int* create(int** arr, int n, int start= 0, int step = 0)
{
    int* a = new int[n];

    for (int i = 0; i < n; i = i ++)
    {
        a[i] = start;
        start += step;
        //cout << a[i] << endl;
    }

    return a;
}

int destroy(int** arr)
{
    if (arr == nullptr)
    {
        return 0;
    }
    if (*arr)
    {
        delete[] * arr;
        *arr = nullptr;
    }
    return 0;
}

void sort(int* array, int length) {
    for (int i = 1; i < length; i++) {
        for (int j = i; j > 0 && array[j - 1] > array[j]; j--) {
            int tmp = array[j - 1];
            array[j - 1] = array[j];
            array[j] = tmp;
        }
    }
}

int* print(int* array, int length)
{
    std::cout << '[';
    for (int i = 0; i < length; i++)
    {
        std::cout << array[i];

        if (i < length - 1)
        {
            std::cout << ", ";
        }
    }

    std::cout << ']' << std::endl;

    return array;
}

int main()
{
    int n, start, step;

    std::cin >> n >> start >> step;

    int* arr = create(&arr, n, start, step);

    sort(arr, n);
    print(arr, n);

    destroy(&arr);
}
