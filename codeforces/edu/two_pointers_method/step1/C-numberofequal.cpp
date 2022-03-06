#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll solve(vector<int> &a, vector<int> &b)
{
    ll c = 0, i = 0;
    ll localc = 0;
    for (int j = 0; j < b.size(); j++)
    {
        if (j > 0 && b[j] == b[j - 1])
        {
            c += localc;
            continue;
        }
        while (i < a.size() && a[i] < b[j])
        {
            i++;
        }
        localc = 0;

        while (i < a.size() && a[i] == b[j])
        {
            i++;
            localc++;
        }
        c += localc;
    }

    return c;
}

int main()
{

    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    vector<int> b(m);
    for (int j = 0; j < m; j++)
    {
        cin >> b[j];
    }

    cout << solve(a, b) << "\n";

    return 0;
}