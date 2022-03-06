#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int n;
ll k;

struct stack
{
    vector<ll> s, smin = {LLONG_MAX}, smax = {LLONG_MIN};

    void push(ll x)
    {
        s.push_back(x);
        smin.push_back(min(smin.back(), x));
        smax.push_back(max(smax.back(), x));
    }

    ll pop()
    {
        ll o = s.back();
        s.pop_back();
        smin.pop_back();
        smax.pop_back();
        return o;
    }

    bool empty()
    {
        return s.empty();
    }

    ll min_()
    {
        return smin.back();
    }

    ll max_()
    {
        return smax.back();
    }
};

::stack sr, sl;

void add(ll x)
{
    sr.push(x);
}

void remove(ll x)
{
    if (sl.empty())
    {
        while (!sr.empty())
        {
            sl.push(sr.pop());
        }
    }
    sl.pop();
}

bool good()
{
    return max(sr.max_(), sl.max_()) - min(sr.min_(), sl.min_()) <= k;
}

ll solve(vector<ll> &a)
{
    ll ans = 0;
    int l = 0;
    for (int r = 0; r < a.size(); r++)
    {
        add(a[r]);
        while (!good())
        {
            remove(a[l]);
            l++;
        }
        ans += r - l + 1;
    }

    return ans;
}

int main()
{

    cin >> n >> k;

    vector<ll> num(n);

    for (int i = 0; i < n; i++)
    {
        cin >> num[i];
    }

    cout << solve(num) << endl;

    return 0;
}