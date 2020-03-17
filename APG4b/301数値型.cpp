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

int main() {
    int N;
    cin >> N;
    ll tmp1 = 2;
    ll tmp2 = 1;
    ll ans = 0;
    if(N == 1){
        cout << 1;
    }
    else {
        for (int i = 1; i < N; i++){
            ans = tmp1 + tmp2;
            tmp1 = tmp2;
            tmp2 = ans;
        }
        cout << ans << endl;
    }
}