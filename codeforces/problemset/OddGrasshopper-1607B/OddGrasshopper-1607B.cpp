#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll solve(ll x, ll n)
{
    ll d = n % 4;

    switch (d)
    {
    case 0:
        d = 0;
        break;
    case 1:
        d = -n;
        break;

    case 2:
        d = 1;
        break;
    case 3:
        d = n + 1;
        break;
    default:
        break;
    }

    return x % 2 == 0 ? x + d : x - d;
}

int main()
{
    int t;
    cin >> t;

    vector<ll> res;

    for (int i = 0; i < t; i++)
    {
        ll x, n;
        cin >> x >> n;
        res.push_back(solve(x, n));
    }

    for (ll e : res)
    {
        cout << e << "\n";
    }
}