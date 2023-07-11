#include <bits/stdc++.h>
using namespace std;
/*
int N; cin >> N;
int H, W; cin >> H >> W;
string str1; cin >> str1;
vector<int> A(N);
for (int i = 0; i < N; i++) cin >> A.at(i);
vector<vector<int>> data1(H, vector<int>(W));
for (int i = 0; i < H; i++) {for (int j = 0; j < W; j++)
{cin >> data1.at(i).at(j);}}
bool flag = false;
*/

int main() {
    int N, W;
    cin >> N >> W;

    // A を B 個並べた配列から大きい順にとっていく
    int A, B;
    vector<pair<int, int>> C;
    for (int i = 0; i < N; i++) {
        cin >> A >> B;
        C.push_back(make_pair(A, B));
    }
    sort(C.rbegin(), C.rend());  // 降順ソートは r つける

    long long oisisa = 0;
    for (auto i = 0; i < N; i++) {
        for (auto j = 0; j < C.at(i).second; j++) {
            oisisa += C.at(i).first;
            W -= 1;
            if (W <= 0) break;
        }
        if (W <= 0) break;
    }

    cout << oisisa << endl;
    return 0;
}
