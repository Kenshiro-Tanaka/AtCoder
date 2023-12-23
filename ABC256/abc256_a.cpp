#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int N;
    cin >> N;
    // 2の累乗はビットシフト
    cout << (1 << N);  // powでやると浮動小数点型になるらしく，intで丸める必要あり

    return 0;
}
