#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll solve(vector<int> &a, int k)
{
    unordered_map<int, int> kb;
    ll ans = 0;

    int l = 0;
    for (int r = 0; r < a.size(); r++)
    {
        unordered_map<int, int>::iterator it = kb.find(a[r]);
        if (it != kb.end())
        {
            it->second++;
        }
        else
        {
            kb.insert(make_pair(a[r], 1));
        }
        while (kb.size() > k)
        {
            unordered_map<int, int>::iterator it = kb.find(a[l]);
            if (it->second > 1)
            {
                it->second--;
            }
            else
            {
                kb.erase(it);
            }
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