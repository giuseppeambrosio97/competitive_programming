#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

/**
 *  The gcd has the following property:
 *          gcd(a,b,c)=gcd(gcd(a,b),c)
 * */

ll gcd(ll a, ll b)
{
    ll mn, mx;
    mn = min(a, b);
    mx = max(a, b);
    while (mn != 0)
    {
        ll r = mx % mn;

        mx = max(r, mn);
        mn = min(r, mn);
    }

    return mx;
}

struct stack
{
    vector<ll> s, s_gcd;

    void push(ll x)
    {
        s.push_back(x);
        s_gcd.push_back(s_gcd.empty() ? x : gcd(x, s_gcd.back()));
    }

    ll pop()
    {
        ll o = s.back();
        s.pop_back();
        s_gcd.pop_back();
        return o;
    }

    ll top()
    {
        return s_gcd.back();
    }

    bool empty()
    {
        return s.empty();
    }
};

::stack sr, sl;

void add(ll x)
{
    sr.push(x);
}

ll remove()
{
    if (sl.empty())
    {
        while (!sr.empty())
        {
            sl.push(sr.pop());
        }
    }
    return sl.pop();
}

bool good()
{
    if (sl.empty())
    {
        return sr.top() == 1;
    }

    if (sr.empty())
    {
        return sl.top() == 1;
    }

    return gcd(sr.top(), sl.top()) == 1;
}

/**
 * This function tells you if we can remove an element of the segmet and after that elimination 
 * the segment keeps being good.
 * */
bool can_remove()
{
    ll removed_el = remove();

    bool res = good();

    sl.push(removed_el);

    return res;
}

int main()
{
    int n;
    cin >> n;
    vector<ll> a(n);

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    int l = 0, ans = INT_MAX;
    for (int r = 0; r < n; r++)
    {
        add(a[r]);
        while (good() && can_remove())
        {
            remove();
            l++;
        }

        if (good())
        {
            ans = min(ans, r - l + 1);
        }
    }

    if (ans == INT_MAX)
    {
        cout << -1 << "\n";
    }
    else
    {
        cout << ans << "\n";
    }

    return 0;
}