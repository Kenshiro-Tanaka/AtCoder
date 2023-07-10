#include <bits/stdc++.h>
using namespace std;
/*
int N; cin >> N;
int H, W; cin >> H >> W;
string str1; cin >> str1;
vector<int> A(200010, 0);
for (int i = 0; i < N; i++) cin >> A.at(i);
vector<vector<int>> data1(H, vector<int>(W));
for (int i = 0; i < H; i++) {for (int j = 0; j < W; j++)
{cin >> data1.at(i).at(j);}}
bool flag = false;
*/
int main() {
    long long A, B;
    cin >> A >> B;

    string flag = "Easy";
    while (A != 0 and B != 0) {
        if ((A % 10) + (B % 10) >= 10) { // 1の位は10で割ったあまりで
            flag = "Hard";
            break;
        } else {
            A /= 10;  // 商を10で割って1桁ずつ減らしていく
            B /= 10;
        }
    }

    cout << flag;
    return 0;
}
