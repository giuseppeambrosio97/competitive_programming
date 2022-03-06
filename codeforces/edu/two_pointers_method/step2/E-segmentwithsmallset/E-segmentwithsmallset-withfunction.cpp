#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

unordered_map<int, int> kb;

void add(int x)
{
    unordered_map<int, int>::iterator it = kb.find(x);
    if (it != kb.end())
    {
        it->second++;
    }
    else
    {
        kb.insert(make_pair(x, 1));
    }
}

void remove(int x)
{
    unordered_map<int, int>::iterator it = kb.find(x);
    if (it->second > 1)
    {
        it->second--;
    }
    else
    {
        kb.erase(it);
    }
}

bool good(int k)
{
    return kb.size() <= k;
}

ll solve(vector<int> &a, int k)
{
    ll ans = 0;
    int l = 0;
    for (int r = 0; r < a.size(); r++)
    {
        add(a[r]);
        while (!good(k))
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

    int n;
    int k;

    cin >> n >> k;

    vector<int> num(n);

    for (int i = 0; i < n; i++)
    {
        cin >> num[i];
    }

    cout << solve(num, k) << endl;

    return 0;
}