#include<iostream>
using namespace std;
int main()
{
    int N;
    int arr[500];

    cin >> N;
    for(int i = 0; i < N; i++)
        cin >> arr[i];
    
    cout << "Before sort: ";
    for(int i = 0; i < N; i++)
        cout << arr[i] << " ";
    
    for(int i = 0; i < N-1; i++)
    {
        for(int j = 0; j < N-1; j++)
        {
            if(arr[j] > arr[j+1])
            {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    cout << endl << "After sort: ";
    for(int i = 0; i < N; i++)
        cout << arr[i] << " ";

    return 0;
}