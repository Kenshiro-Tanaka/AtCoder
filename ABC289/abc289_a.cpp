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
deque<int> deq;
bool flag = false;
for (auto&& a:A) cin >> a;
*/
int main() {
    string s;
    cin >> s;

    for (auto c : s) {
        if (c == '0') {
            cout << '1';
        } else {
            cout << '0';
        }
    }

    cout << endl;

    return 0;
}
