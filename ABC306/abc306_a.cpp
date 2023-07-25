#include <bits/stdc++.h>
using namespace std;
/*
int N; cin >> N;
int H, W; cin >> H >> W;
string str1; cin >> str1;
vector<int> A(200010, 0);
for (int i = 0; i < N; i++) cin >> A.at(i);
vector<vector<int>> data1(H, vector<int>(W));
for (int i = 0; i < H; i++) {for (int j = 0; j < W; j++) {cin >>
data1.at(i).at(j);}} bool flag = false;
*/
int main() {
    int N;
    cin >> N;
    string str1;
    cin >> str1;

    for (auto c : str1) {
        cout << c << c;  // 同じ文字を繰り返して出力するだけ
    }
    return 0;
}
