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
    vector<vector<long long>> data1(N, vector<long long>(2));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < 2; j++) {
            cin >> data1.at(i).at(j);
        }
    }

    sort(data1.begin(), data1.end());

    long long pos = 0;
    pos = K;  // はじめの所持金分は必ず進める
    for (int i = 0; i < N; i++) {
        long long friends = data1.at(i).at(0);
        long long money = data1.at(i).at(1);
        if (pos >= friends) {  // 友達がposと同じか左にいたら
            pos += money;      // お金を回収と同時に移動
        } else {
            break;
        }
    }

    cout << pos << endl;

    return 0;
}
