#include <bits/stdc++.h>

using namespace std;

int solve(vector<int> a)
{
    int sec = a.at(0) + 2 * a.size() - 1;

    for (int i = 1; i < a.size(); i++)
    {
        sec += abs(a.at(i) - a.at(i - 1));
    }
    return sec;
}

int main()
{
    int n;
    cin >> n;

    vector<int> a;

    while (n--)
    {
        int v;
        cin >> v;
        a.push_back(v);
    }

    cout << solve(a);
}