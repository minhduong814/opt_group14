#include<bits/stdc++.h>
using namespace std;

const int N = 1e3 + 5;
int n, m, b, max_load, a[N][N], load[N], ans[N][N], tmp[N][N]; 

void print_ans() {
    cout << n << '\n';
    for(int i = 1; i <= n ; i++) {
        cout << b << ' ';
        for(int j = 1 ; j <= b; j++) 
            cout << ans[i][j] << ' ';
        cout << '\n';
    }
}

void solution() {
    max_load = 0;
    for(int i = 1; i <= n ; i++)
        for(int j = 1; j <= b; j++) {
            ans[i][j] = tmp[i][j];
            max_load = max(max_load, load[ans[i][j]]);
        }
}

void branch_and_bound(int i, int j, int k) {    // j-th reviewer of i-th paper
    if(i == n + 1) {
        solution();
    }
    for(int c = 0; c <= 1; c++) {
        load[a[i][j]] += c;
        k += c;
        // branch and bound
        if(load[a[i][j]] < max_load && k <= b && a[i][0] - j + k >= b) {
            if(c == 1) tmp[i][k] = a[i][j];
            if(j == a[i][0]) {
                if(k == b)
                    branch_and_bound(i + 1, 1, 0);
            }
            else                  
                branch_and_bound(i, j + 1, k);
        }
        load[a[i][j]] -= c;
        k -= c;
    }
}

int main() {
    cin >> n >> m >> b;
    for(int i = 1; i <= n ; i++) {
        cin >> a[i][0];
        for(int j = 1 ; j <= a[i][0]; j++)
            cin >> a[i][j];
    }
    max_load = n + 1;
    branch_and_bound(1, 1, 0);
    print_ans();
    cout << max_load;
}