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
    int N;
    cin >> N;

    // 5で割って余りが0,1,2ならその値に*5,そうでないならその値に+1してから*5
    int n = N / 5;
    int r = N % 5;
    int result = 0;

    if (r == 3 || r == 4) {
        result = (n + 1) * 5;
    } else {
        result = n * 5;
    }

    cout << result << endl;

    return 0;
}
