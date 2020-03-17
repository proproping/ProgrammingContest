#include <bits/stdc++.h>
using namespace std;

int main() {
    int x,a,b;
    cin >> x >> a >> b;
    cout << ++x << endl;
    int tmp = x*(a+b);
    cout << tmp << endl;
    tmp *= tmp;
    cout << tmp << endl;
    cout << tmp-1 << endl;
}