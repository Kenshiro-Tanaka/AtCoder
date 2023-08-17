#include <bits/stdc++.h>
using namespace std;

/*
int sub() {
    int N;
    cin >> N;

    int H, W;
    cin >> H >> W;

    string str1;
    cin >> str1;

    vector<int> A(200010, 0);
    for (int i = 1; i <= N; i++) cin >> A[i];

    vector<vector<int>> data1(H, vector<int>(W));
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            cin >> data1.at(i).at(j);
        }
    }

    bool flag = false;
}
*/

int main() {
    string S;
    cin >> S;

    for (auto& c : S) {
        c = toupper(c);
    }
    cout << S << endl;

    return 0;
}
