#include <bits/stdc++.h>
using namespace std;

int main() {
    int L, R;
    cin >> L >> R;
    string str = "atcoder";
    string ans;

    // str.substr()を使えば楽
    for (int i = L - 1; i < R; i++) {
        ans += str[i];
    }
    cout << ans << endl;

    return 0;
}
