#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    int count = 0;
    char str[500];
    scanf("%[^\n]", str);
    for(int i = 0; i < strlen(str); i++)
    {
        if(str[i] == ';')
            count++;
    }
    cout << "counter = " << count;
    return 0;
}