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
    int N, K;
    cin >> N >> K;
    vector<int> P(N);  // 3日分の和を入れる1次元配列
    int a, b, c;       // 3日分の和を出すための入力用
    for (int i = 0; i < N; i++) {
        cin >> a >> b >> c;
        P.at(i) = a + b + c;
    }

    vector<int> A(N);  // 比較するためにPのコピーを持っておきたい
    A = P;

    sort(P.rbegin(), P.rend());  // Pを降順ソートすれば上位K位の人の点数が調べられる
    for (int i = 0; i < N; i++) {
        if (A.at(i) + 300 >= P.at(K - 1)) {  // ありえるかどうかだからi番目の人だけが満点でいい
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }

    return 0;
}
