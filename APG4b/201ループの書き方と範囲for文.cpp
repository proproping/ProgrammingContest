#include <bits/stdc++.h>
#define _GLIBCXX_DEBUG
#define rep(i,n) for (int i = 0; i< (int)(n); i++)
using namespace std;

int main() {
    vector<int> A(5);
    bool flag = false;
    for (int i = 0; i < 5; i++){
        cin >> A[i];
    }
    for (int i = 1; i < A.size(); i++){
        if (A[i] == A[i-1]) {
            flag = true;
            break;
        }
    }
    if (flag) {
        cout << "YES" << endl;
    }
    else {
        cout << "NO" << endl;
    }
}