#include <iostream>

struct IntArray {
    int* data;
    int size;
};

void create(IntArray* arr, int size) {
    arr->data = new int[size]();
    arr->size = size;
}

void create(IntArray& arr, int size) {
    arr.data = new int[size]();
    arr.size = size;
}

int get(IntArray& arr, int index)
{
    if (index < 0 || index >= arr.size){
        std::cout << "Ошибка, выхрод за границу массива. Работа программы завершена";
        exit(1);
    }
    return arr.data[index];
}
int get(IntArray* arr, int index)
{
    return get(*arr, index);
}

void set(IntArray& arr, int index, int value)
{
    if (index < 0 || index >= arr.size){
        std::cout << "Ошибка, выхрод за границу массива. Работа программы завершена";
        exit(1);
    }
    arr.data[index] = value;
}
void set(IntArray* arr, int index, int value)
{
    set(*arr, index, value);
}

void resize(IntArray* arr, int newSize) {
    int* newArr = new int[newSize];

    if (newSize < arr->size) {
        for (int i = 0; i < newSize; i++)
            newArr[i] = arr->data[i];
    }
    else { // newSize >= arr->size
        for (int i = 0; i < arr->size; i++)
            newArr[i] = arr->data[i];
        for (int i = arr->size; i < newSize; i++)
            newArr[i] = 0;
    }

    delete arr->data;
    arr->data = newArr;
    arr->size = newSize;
}
void resize(IntArray& arr, int newSize)
{
    resize(&arr, newSize);
}

void destroy(IntArray& arr)
{
    if (!arr.data)
    {
        delete[] arr.data;
        arr.data = nullptr;
    }
    arr.size = 0;
}
void destroy(IntArray* arr)
{
    destroy(*arr);
}

void print(IntArray& arr)
{
    if (arr.size == 0)
    {
        puts("[]");
        return;
    }
    if (arr.size < 0)
    {
        return;
    }
    printf("[%d", get(arr, 0));
    for (int i = 1; i < arr.size; ++i)
        printf(", %d", get(arr, i));
    printf("]\n");
}
void print(IntArray* arr)
{
    print(*arr);
}

int main()
{
    std::cout << "Hello World!\n";
    
    IntArray arr = {};
    create(arr, 30);
    for (int i = 0; i < 30; i++) {
        set(arr, i, i + 1);
    }
    print(arr);
    resize(arr, 50);
    print(arr);
    resize(arr, 10);
    print(arr);
    destroy(arr);
}
