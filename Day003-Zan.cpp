#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    char str[500];
    cin >> str;
    for(int i = 0; i < strlen(str); i++)
    {
        if(str[i] == 'z')
            printf("a");
        else if(str[i] == 'Z')
            printf("A");
        else 
            printf("%c", str[i]+1);
    }
    return 0;
}