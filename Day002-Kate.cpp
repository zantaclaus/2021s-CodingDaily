#include<iostream>
using namespace std;

int main()
{
    int x;
    cin >> x;

    if(x == 0)
        cout << "1";
    else if(x < 0)
        cout << "-1";
    else 
        cout << x*100 + 1;
    
    return 0;
}