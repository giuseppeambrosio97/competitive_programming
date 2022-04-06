#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

pair<ll, ll> random_grid(ll r, ll c)
{
    ll row = rand() % r;
    ll col = rand() % c;
    return make_pair(row, col);
}

vector<pair<ll, ll>> k_random_grid(ll k, ll r, ll c)
{
    vector<pair<ll, ll>> pairs(k);
    for (ll i = 0; i < k; i++)
    {
        pairs[i] = random_grid(r, c);
    }
    return pairs;
}

int main()
{
    srand(time(0));
    vector<pair<ll, ll>> p = k_random_grid(5, 10, 10);

    for (pair<ll, ll> e : p)
    {
        cout << "(" << e.first << "," << e.second << ")\n";
    }
}