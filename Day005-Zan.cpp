#include<iostream>
using namespace std;
int main()
{
    float sum = 0;
    int N, input;

    cin >> N;
    for(int i = 0; i < N; i++)
    {
        cin >> input;
        sum += input;
    }
    printf("Average = %.2f", sum/N);
    return 0;
}