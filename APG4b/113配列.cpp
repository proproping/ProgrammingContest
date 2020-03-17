#include <bits/stdc++.h>
#define _GLIBCXX_DEBUG
using namespace std;

int main() {
    int N,ave,sum,ans;
    cin >> N;
    vector<int> a(N);
    for (int i = 0; i < N; i++){
        cin >> a.at(i);
        sum += a.at(i);
    }
    ave = sum/N;
    for (int i = 0; i < N; i++){
        ans = a.at(i) - ave;
        if (ans < 0){
            cout << -ans << endl;
        }
        else {
            cout << ans << endl;
        }
    }
    
}