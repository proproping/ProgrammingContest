#include <bits/stdc++.h>
#define _GLIBCXX_DEBUG
#define rep(i,n) for (int i = 0; i< (int)(n); i++)
using namespace std;

int main() {
    int a,b,c,mi,ma;
    cin >> a >> b >> c;
    mi = min(min(a,b),c);
    ma = max(max(a,b),c);
    cout << ma - mi << endl;
}