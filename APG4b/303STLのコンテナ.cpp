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
    ll N;
    cin >> N;
    map<ll,ll> dic;
    for (ll i = 0; i < N; i++){
        ll key ;
        cin >> key;
        dic[key] += 1;
    }
    vector<P> ans(N);
    ll i = 0;
    for (auto p : dic){
        auto k = p.first;
        auto v = p.second;
        ans[i].first = v;
        ans[i].second = k;
        i += 1;
    }
    sort(RALL(ans));
    cout << ans[0].second << " " << ans[0].first << endl;
}