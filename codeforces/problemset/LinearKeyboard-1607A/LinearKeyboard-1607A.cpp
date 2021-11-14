#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int solve(unordered_map<char, int> kb, string s)
{
    int o = 0;

    for (int i = 1; i < s.length(); i++)
    {
        int t = kb.at(s.at(i)) - kb.at(s.at(i - 1));
        o += abs(t);
    }

    return o;
}

int main()
{
    int t;
    cin >> t;

    vector<int> res;

    while (t--)
    {
        string s;
        unordered_map<char, int> kb;

        for (int i = 1; i <= 26; i++)
        {
            char ch;
            cin >> ch;
            kb.insert(make_pair(ch, i));
        }

        cin >> s;
        res.push_back(solve(kb, s));
    }

    for (int e : res)
    {
        cout << e << "\n";
    }

    return 0;
}