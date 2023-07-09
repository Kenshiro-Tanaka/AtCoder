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
    string S;
    cin >> S;

    // 全ての文字の出現回数を調べるやり方
    map<char, int> mp;  // 連想配列はPythonでいう辞書のように使える
    for (auto i : S) {
        mp[i] += 1;
    }
    string flag = "-1";
    for (char i = 'a'; i <= 'z'; i++) {  // forでASCIIを回せるのか
        if (mp[i] == 1) {
            flag = i;
            break;
        }
    }
    cout << flag << endl;

    return 0;
}
