// travelling by stagecoach

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
  int n,m,a,b,k;
  int t[8];
  int d[30][30];
  cin >> n >> m >> k >> a >> b;
  rep(i,n){
    cin >> t[i];
  }
  rep(i,m) rep(j,m) d[i][j] = -1;
  rep(i,k){
    int A,B,c;
    cin >> A >> B >> c;
    d[A-1][B-1] = c;
    d[B-1][A-1] = c;
  }
  double dp[1 << 8][30];
  for (int i = 0 ; i < 1 << n; i++){
    fill(dp[i], dp[i] + m, INF);
  }
  dp[(1 << n) - 1][a - 1] = 0;
  double res = INF;
  for (int S = (1 << n) - 1; S >= 0; S--){
    res = min(res,dp[S][b-1]);
    for (int v = 0; v < m; v++){
      for (int i = 0; i < n; i++){
        if (S >> i & 1){
          for (int u= 0; u < m; u++){
            if (d[v][u] >= 0) {
              dp[S & ~ (1 << i)][u] = min(dp[S & ~ (1 << i)][u], dp[S][v]+ (double)d[v][u]/t[i]);
            }
          }
        }
      }
    }
  }
  if (res == INF){
    printf("Impossible\n");
  } else {
    printf("%.3f\n",res);
  }
}