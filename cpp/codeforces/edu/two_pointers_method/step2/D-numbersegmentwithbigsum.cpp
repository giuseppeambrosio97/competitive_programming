#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll solve(vector<int> &a, ll s)
{
    int l = 0;
    ll ans = 0;
    ll sum = 0;

    for (int r = 0; r < a.size(); r++)
    {
        sum += a[r];
        while (sum >= s)
        {
            /********************************
             *  when you reach the last l after which the segment is no longer good you stop the process and don't delete it!
             *  so the process of deletion of a[l] continue until we find the last good couple, where the last good couple is defined as follow:
             *  1) sum(a[i]...a[r])    >= s  good
             *  2) sum(a[i-1]...a[r])  <  s   not good
             * ******************************/
            sum -= a[l];
            l++;
        }
        ans += l;
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