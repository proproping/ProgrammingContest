#include <bits/stdc++.h>
using namespace std;

int main() {
    int pt;
    cin >> pt;
    if (pt == 1){
        int pr,N;
        cin >> pr >> N;
        cout << pr * N << endl;
    }
    else{
        string text;
        int pr,N;
        cin >> text >> pr >> N;
        cout << text+"!" << endl;
        cout << pr * N << endl;
    }
}