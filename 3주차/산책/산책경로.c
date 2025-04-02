#include <bits/stdc++.h>
using namespace std;
int n;
long long ans;
bool visited[200001];
string s;
vector<int> adj[200001], v;
void dfs(int p) {
    int cnt=0;
    for(auto x: adj[p]) {
        if(s[x-1]=='0' && !visited[x]) {
            visited[x]=1;
            dfs(x);
        }
        if(s[x-1]=='1') cnt++;
    }
    v.push_back(cnt);
}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> s;
    for(int i=0; i<n-1; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
        if(s[a-1]=='1' && s[b-1]=='1') ans+=2;
    }
    for(int i=1; i<=n; i++) {
        if(!visited[i] && s[i-1]=='0') {
            long long sum=0;
            v.clear();
            visited[i]=1;
            dfs(i);
            for(int j=0; j<(int)v.size(); j++) sum+=(long long)v[j];
            ans+=sum*sum-sum;
        }
    }
    cout << ans;
}