#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        string prefix = "";

        int i = 0;
        bool good = true;
        while (good)
        {
            if (strs[0].size() > i)
            {
                for (int j = 1; j < strs.size(); j++)
                {
                    if (strs[j].size() > i)
                    {
                        if (strs[j].at(i) != strs[0].at(i))
                        {
                            good = false;
                        }
                    }
                    else
                    {
                        good = false;
                    }
                }
            }
            else
            {
                good = false;
            }

            if (good)
            {
                prefix.push_back(strs[0][i]);
            }
            i++;
        }
        return prefix;
    }
};
