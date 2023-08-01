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
    int N;
    cin >> N;
    int a;
    for (int i = 0; i < N; i++) {  // 全て入力しなくても逐次処理でいい
        cin >> a;
        if (a % 2 == 0) cout << a << " ";
    }
    cout << endl;

    return 0;
}
