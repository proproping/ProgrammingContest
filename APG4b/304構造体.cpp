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

struct Clock{
    int hour;
    int minute;
    int second;

    void set(int h, int m,int s){
        hour = h;
        minute = m;
        second = s;
        return;
    }

    string to_str(){
        string H, M, S;
        H = to_string(hour);
        M = to_string(minute);
        S = to_string(second);
        if (H.size() == 1){
            H = "0"+H;
        }
        if (M.size() == 1){
            M = "0"+M;
        }
        if (S.size() == 1){
            S = "0"+S;
        }
        return H+":"+M+":"+S;
    }

    void shift(int diff_second){
        int sec = hour*3600 + minute*60 + second;
        sec += diff_second;
        sec %= 86400;
        if (sec < 0){
            sec += 86400;
        }
        hour = sec/3600;
        minute = (sec/60)%60;
        second = sec%60;
    }
};

int main(){
    int hour,minute,second;
    cin >> hour >> minute >> second;
    int diff_second;
    cin >> diff_second;
    Clock clock;
    clock.set(hour,minute,second);
    cout << clock.to_str() << endl;
    clock.shift(diff_second);
    cout << clock.to_str() << endl;
}