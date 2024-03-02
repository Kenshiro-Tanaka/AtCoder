#include <bits/stdc++.h>
using namespace std;

int main(void){
    int K, X;
    cin >> K >> X;
    if (500 * K >= X){
        cout << "Yes"; // ''は1文字の場合
    }else{
        cout << "No";
    }
    
    return 0;
}
