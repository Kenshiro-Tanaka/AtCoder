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
    vector<int> A(5);
    for (int i = 0; i < 5; i++) cin >> A.at(i);

    sort(A.begin(), A.end());
    // ソートすればフルハウスである条件はこうなる
    string ans = (A[0] == A[2] and A[3] == A[4]) ? "Yes" : (A[0] == A[1] and A[2] == A[4]) ? "Yes"
                                                                                           : "No";
    cout << ans;

    return 0;
}
