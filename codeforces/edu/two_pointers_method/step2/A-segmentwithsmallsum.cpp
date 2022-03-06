#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int solve(vector<int> &a, ll s)
{
    int l = 0, ans = 0;
    ll sum = 0;

    for (int r = 0; r < a.size(); r++)
    {
        sum += a[r];
        while (sum > s)
        {
            sum -= a[l];
            l++;
        }
        ans = max(ans, r - l + 1);
    }

    return ans;
}

int main()
{

    int n;
    ll s;

    cin >> n >> s;

    vector<int> num(n);

    for (int i = 0; i < n; i++)
    {
        cin >> num[i];
    }

    cout << solve(num, s) << endl;

    return 0;
}