#include<iostream>
using namespace std;
int main()
{
    int N, x;
    int max = -99999, min = 99999;
    
    cin >> N;
    for(int i = 0; i < N; i++) {
        cin >> x;
        if(x < min)
            min = x;
        if(x > max)
            max = x;
    }

    cout << "max - min = "<< max - min;

    return 0;
}