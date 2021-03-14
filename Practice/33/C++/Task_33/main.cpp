#include <iostream>

using namespace std;

int* create(int length,  int init=0, int step=0)
{
    int *darr = new int[length];
    for (int i = 0; i < length; i++) {

        darr[i] = init + ((i+1)-1)*step;
    }

    return darr;
}

void sort(int* array,int length){
    for(int i=1;i<length;i++){
        for(int j=i; j>0 && array[j-1]>array[j];j--){
            int tmp=array[j-1];
            array[j-1]=array[j];
            array[j]=tmp;
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
            std::cout <<", ";
        }
    }

    std::cout << ']' << std::endl;

    return array;
}

int main()
{

    int length, init, step;

    std::cin >> length >> init >> step;

    int*  d_array = create(length, init, step);
    sort(d_array, length);
    print(d_array, length);

    delete[] d_array;

    return 0;
}
