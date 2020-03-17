#include <bits/stdc++.h>
#define _GLIBCXX_DEBUG
#define rep(i,n) for (int i = 0; i< (int)(n); i++)
using namespace std;

int main() {
    int N,M;
    cin >> N >> M;
    vector<int> A(M),B(M);
    vector<vector<string>> R(N, vector<string>(N, "-"));
    vector<vector<int>> res(M,vector<int>(2));
    for (int i = 0; i < M; i++){
        for (int j = 0; j < 2; j++){
            cin >> res[i][j];
        }
    }
    for (int i =0; i < M; i++){
        int win;
        int lose;
        win = res[i][0]-1;
        lose = res[i][1]-1;
        R[win][lose] = "o";
        R[lose][win] = "x";
    }
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            cout << R[i][j];
            if (j != N-1){
                cout << " ";
            }
        }
        cout << endl;
    }
}