#include<iostream>
using namespace std;
int abs(int number){
    if (number > 0)
        return number;
    return -number;
}

int main()
{
    int n;
    cin >> n;
    int metrix[n][n];
    int sum = 0;
    for(int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> metrix[i][j];
            if (i == j)
                sum += metrix[i][j];
            if (i + j == n - 1)
                sum -= metrix[i][j];
        }
    }
    cout << abs(sum);
    return 0;
}