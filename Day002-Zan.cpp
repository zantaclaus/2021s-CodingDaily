#include<iostream>
using namespace std;
int main()
{
    int N = 0;
    int ans = 0;
    bool check = false;
    
    cin >> N;
    for(int i = 2; i <= N; i++){
        check = false;
        for(int j = 2; j < i; j++){
            if(i % j == 0){
                check = true;
                break;
            }
        }
        if(check) 
            continue;
        ans++;
        cout << i << endl;
    }
    cout << "Count = " << ans;
    return 0;
}