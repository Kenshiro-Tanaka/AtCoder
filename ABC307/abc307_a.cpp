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
    int N;  // Nは週
    cin >> N;
    vector<int> A(N * 7);
    for (int i = 0; i < N * 7; i++) cin >> A.at(i);

    vector<int> B(N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < 7; j++)
            B.at(i) += A.at(i * 7 + j);
    }

    for (int i = 0; i < N; i++) cout << B.at(i) << ' ';

    return 0;
}
