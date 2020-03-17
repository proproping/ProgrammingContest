#include <bits/stdc++.h>
#define _GLIBCXX_DEBUG
#define rep(i,n) for (int i = 0; i < (int)(n); i++)
#define rep1(i,n) for (int i = 1; i <= n; ++i)
#define ALL(v) v.begin(), v.end()
#define RALL(v) v.rbegin(), v.rend()
#define EPS (1e-7)
#define INF (1e9)
#define PI (acos(-1))
using namespace std;
typedef long long ll;
typedef pair<ll, ll> P;
template<class T> inline bool chmin(T& a, T b) {
    if (a > b) {
        a = b;
        return true;
    }
    return false;
}
template<class T> inline bool chmax(T& a, T b) {
    if (a < b){
        a = b;
        return true;
    }
    return false;
}

int main(){
    int N;
    cin >> N;
    vector<P> ls(N);
    for (int i = 0; i < N; i++){
        cin >> ls[i].second >> ls[i].first;
    }
    sort(ALL(ls));
    for (int i = 0; i < N; i++){
        cout << ls[i].second << " " << ls[i].first << endl;
    }


}