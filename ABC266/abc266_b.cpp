#include <bits/stdc++.h>
using namespace std;
/*
int N; cin >> N;
int H, W; cin >> H >> W;
string str1; cin >> str1;
vector<int> A(N), B(N);
for (int i = 0; i < N; i++) cin >> A.at(i) >> B.at(i);
vector<vector<int>> data1(H, vector<int>(W));
for (int i = 0; i < H; i++) {for (int j = 0; j < W; j++)
{cin >> data1.at(i).at(j);}}
bool flag = false;
for (auto&& a:A) cin >> a;
*/
int main() {
    long long N;
    cin >> N;
    for (long long i = 0; i < 998244354; i++) {
        if ((N - i) % 998244353 == 0) {
            cout << i;
            break;
        }
    }
    return 0;
}

// N - x = 0 (mod m) なら N = x (mod m)
// だからPythonなら N % 998244353 でいいけど
// c++は負の数に対する余りが負になる場合に注意
