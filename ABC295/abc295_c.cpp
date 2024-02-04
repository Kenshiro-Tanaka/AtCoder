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

#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    map<int, int> mp;  // mapはO(logN)
    for (int i = 0; i < N; i++) {
        int a;
        cin >> a;
        mp[a]++;
    }

    int ans = 0;
    for (auto x : mp) {       // mapはキーと値のペアなのでx.secondで値を参照できる
        ans += x.second / 2;  // ペア数は /2
    }

    cout << ans << endl;

    return 0;
}
