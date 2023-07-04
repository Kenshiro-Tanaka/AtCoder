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
    long long N, A, B;
    cin >> N >> A >> B;
    long long P, Q, R, S;
    cin >> P >> Q >> R >> S;

    // (A+k, B+k)から傾きが45度の直線上に並ぶことがわかる
    for (long long i = P; i < Q + 1; i++) {
        for (long long j = R; j < S + 1; j++) {
            // kとlを(A, B), (i, j)の差分として定義
            long long k = i - A;
            long long l = j - B;
            // k==lなら(A, B)を通り，傾きが45度の直線上に
            // (i, j) が存在することになる
            if (k >= max(1 - A, 1 - B) && k <= min(N - A, N - B) && k == l)
                cout << '#';
            else if (k >= max(1 - A, B - N) && k <= min(N - A, B - 1) && k == -l)
                cout << '#';
            else
                cout << '.';
        }
        cout << endl;
    }
    return 0;
}
