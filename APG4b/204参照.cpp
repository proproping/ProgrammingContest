#include <bits/stdc++.h>
#define _GLIBCXX_DEBUG
#define rep(i,n) for (int i = 0; i< (int)(n); i++)
using namespace std;

void saiten(vector<vector<int>> &mat,int &cc,int &wc){
    for (int i = 0; i < 9; i++){
        for (int j = 0; j < 9; j++){
            if (mat[i][j] != (i+1)*(j+1)){
                mat[i][j] = (i+1)*(j+1);
                wc += 1;
            }
            else {
                cc += 1;
            }
        }
    }
}
int main(){
    vector<vector<int>> A(9,vector<int>(9));
    for (int i = 0; i < 9; i++){
        for (int j = 0; j < 9; j++){
            cin >> A[i][j];
        }
    }

    int correct_count = 0;
    int wrong_count = 0;

    saiten(A,correct_count,wrong_count);

    for (int i = 0; i < 9; i++){
        for (int j = 0; j < 9; j++){
            cout << A[i][j];
            if (j < 8){
                cout << " ";
            }
            else {
                cout << endl;
            }
        }
    }

    cout << correct_count << endl;
    cout << wrong_count << endl;
}