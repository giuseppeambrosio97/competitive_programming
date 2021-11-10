#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll solve(ll n, vector<ll> a)
{
    sort(a.begin(), a.end());
    int i = 0;

    ll m = a.at(0);

    while (i < n)
    {
        // cout << " del " << a.at(i) << "\n";
        // cout << "new array \n";
        for (int j = i + 1; j < n; j++)
        {
            a.at(j) -= a.at(i);
            // cout << a.at(j) << " \n";
        }
        i++;

        if (i < n && a.at(i) > m)
        {
            m = a.at(i);
        }
    }
    return m;
}

ll solve2(int n, vector<ll> a)
{
    sort(a.begin(), a.end());
    ll m = a.at(0);

    int i = 1;

    while (i < n)
    {
        ll ai = a.at(i) - a.at(i - 1);
        if (ai > m)
        {
            m = ai;
        }
        i++;
    }
    return m;
}

int main()
{
    int t;

    cin >> t;

    vector<ll> res;

    for (int i = 0; i < t; i++)
    {
        ll n;
        cin >> n;
        vector<ll> a;
        for (int j = 0; j < n; j++)
        {
            ll el;
            cin >> el;
            a.push_back(el);
        }
        res.push_back(solve2(n, a));
    }

    for (ll e : res)
    {
        cout << e << "\n";
    }
    return 0;
}