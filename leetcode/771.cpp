#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution
{
public:
    int numJewelsInStones_array(string jewels, string stones)
    {
        int h[128]={0};

        for (char ch : stones)
        {
            h[ch]++;
        }
        int cnt = 0;

        for (char ch : jewels)
        {
            cnt += h[ch];
        }

        return cnt;
    }

    int numJewelsInStones(string jewels, string stones)
    {
        unordered_map<char, int> h;

        for (char ch : stones)
        {
            h[ch]++;
        }
        int cnt = 0;

        for (char ch : jewels)
        {
            cnt += h[ch];
        }

        return cnt;
    }
};