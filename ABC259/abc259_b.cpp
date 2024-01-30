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

#define PI 3.14159265358979

int main() {
    int a, b, d;
    cin >> a >> b >> d;

    long double A, B, rd;
    rd = d * PI / 180;

    A = a * cos(rd) + b * (-sin(rd));
    B = a * sin(rd) + b * cos(rd);

    cout.precision(20);
    cout << A << ' ' << B << endl;

    return 0;
}

// 回転行列
// x' = cos -sin  x
// y'   sin  cos  y
