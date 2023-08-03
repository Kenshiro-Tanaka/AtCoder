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
    vector<int> S(N);
    for (int i = 0; i < N; i++) cin >> S.at(i);

    // ありえる答えの集合を作る（答え<=1000で）
    int cnt = 0;
    set<int> st;
    for (int a = 1; a <= 143; a++) {  // b=1のときの4ab+3a+3b<=1000を解いてa<=143
        for (int b = 1; b <= 143; b++) {
            if (4 * a * b + 3 * a + 3 * b <= 1000) {  // 1000以下だけを保存
                st.insert(4 * a * b + 3 * a + 3 * b);
            }
        }
    }
    // N人に対して集合の中にあるかを聞いていく
    for (int i = 0; i < N; i++) {
        if (st.find(S.at(i)) == st.end()) {
            cnt++;
        }
    }

    cout << cnt;

    return 0;
}

// 別解
// i番目の情報に対してbを固定したときのaが正の整数であればよい
// float a = 0;
// for (int i = 0; i < N; i++) {
//     for (int b = 1; b < 1000; b++) {
//         a = (S.at(i) - 3 * b) / (4 * b + 3);
//         if (a > 0 && (S.at(i) - 3 * b) % (4 * b + 3) == 0) { // Pythonならできるint(a) == aができない
//             cnt++;
//             break;
//         }
//     }
// }
// cout << N - cnt << endl; // 合っている人をカウントしたので
