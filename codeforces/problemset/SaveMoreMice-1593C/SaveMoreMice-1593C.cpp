#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll search(ll k, vector<ll> mice, ll f[])
{
    ll l = 0, u = k - 1;
    ll med = (l + u) / 2;
    while (u - l + 1 > 1)
    {
        // cout << "\nmed\n"
        //      << med << "\n";
        if (f[med] < mice.at(med))
        {
            if (med == 0)
            {
                return k;
            }
            else if (f[med - 1] >= mice.at(med - 1))
            {
                return k - med;
            }
            else
            {
                u = med - 1;
            }
        }
        else
        {
            l = med + 1;
        }
        med = (l + u) / 2;
    }

    return k - med;
}

// ll search(ll k, vector<ll> mice, ll f[])
// {
//     ll j = k - 1;
//     while (j >= 0)
//     {
//         if (f[j] <= mice.at(j) && f[j-1] <= mice.at(j-1))
//             j--;
//     }

//     cout << "\nj\n"
//          << j;
//     return k - 1 - j;
// }

int main()
{
    int t;
    cin >> t;
    vector<ll> res;

    while (t--)
    {
        ll n, k;
        cin >> n >> k;
        vector<ll> mice;
        for (ll j = 0; j < k; j++)
        {
            ll v;
            cin >> v;
            mice.push_back(v);
        }

        sort(mice.begin(), mice.end());

        ll f[k];

        f[k - 1] = 0;

        for (ll i = k - 2; i >= 0; i--)
        {
            f[i] = f[i + 1] + (n - mice.at(i + 1));
        }

        res.push_back(search(k, mice, f));
    }

    for (ll e : res)
    {
        cout << e << "\n";
    }
}