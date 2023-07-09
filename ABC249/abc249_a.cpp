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
    int A, B, C, D, E, F, X;
    cin >> A >> B >> C >> D >> E >> F >> X;
    // xy図書いたら分かる
    int loopt = X / (A + C);
    int loopa = X / (D + F);
    int dt = (X % (A + C) >= A) ? loopt * A * B + A * B
                                : loopt * A * B + (X % (A + C)) * B;
    int da = (X % (D + F) >= A) ? loopa * D * E + D * E
                                : loopa * D * E + (X % (D + F)) * E;

    string result = dt > da ? "Takahashi" : dt < da ? "Aoki"
                                                    : "Draw";
    cout << result << endl;

    return 0;
}
