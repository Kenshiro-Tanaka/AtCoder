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
char c[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

int main() {
    int H, W;
    cin >> H >> W;

    int a;
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            cin >> a;
            if (a == 0) {
                cout << ".";
            } else {
                cout << c[a - 1];
            }
        }
        cout << endl;
    }

    return 0;
}
