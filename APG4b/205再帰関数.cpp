#include <bits/stdc++.h>
#define _GLIBCXX_DEBUG
#define rep(i,n) for (int i = 0; i< (int)(n); i++)
using namespace std;

int count_report_num(vector<vector<int>> &chil, int x){
    if (chil[x].size() == 0){
        return 1;
    }
    int rr = 0;
    for (int c : chil[x]){
        rr += count_report_num(chil,c);
    }
    rr += 1;
    return rr;
}

int main() {
    int N;
    cin >> N;

    vector<int> P(N);
    P[0] = -1;
    for (int i = 1; i < N; i++){
        cin >> P[i];
    }

    vector<vector<int>> chil(N);
    for (int i = 1; i < N; i++){
        int par = P[i];
        chil[par].push_back(i);
    }

    for (int i = 0; i < N; i++){
        cout << count_report_num(chil,i) << endl;
    }
}