#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, X;
    cin >> N >> X;
    string str;

    // A to Zの配列を作る
    for (char moji = 'A'; moji <= 'Z'; ++moji) {
        for (int i = 0; i < N; i++) {
            str += moji;
        }
    }
    cout << str[X - 1] << endl;

    return 0;
}
