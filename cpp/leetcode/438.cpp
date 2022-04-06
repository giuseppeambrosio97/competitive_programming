#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    vector<int> findAnagrams(string s, string p)
    {
        int np = p.size(), ns = s.size();
        vector<int> ans;
        if (np > ns)
        {
            return ans;
        }

        int countp[26] = {0}, counts[26] = {0};

        for (int i = 0; i < np; i++)
        {
            countp[p[i] - 'a']++;
            counts[s[i] - 'a']++;
        }

        int matches = 0;
        for (int i = 0; i < 26; i++)
        {
            if (counts[i] == countp[i])
            {
                matches++;
            }
        }

        if (matches == 26)
        {
            ans.push_back(0);
        }

        for (int r = np, l = 0; r < ns; r++, l++)
        {
            counts[s[r] - 'a']++;
            if (counts[s[r] - 'a'] == countp[s[r] - 'a'])
            {
                matches++;
            }
            else if (counts[s[r] - 'a'] - 1 == countp[s[r] - 'a'])
            {
                matches--;
            }

            counts[s[l] - 'a']--;
            if (counts[s[l] - 'a'] == countp[s[l] - 'a'])
            {
                matches++;
            }
            else if (counts[s[l] - 'a'] + 1 == countp[s[l] - 'a'])
            {
                matches--;
            }
            if (matches == 26)
            {
                ans.push_back(l+1);
            }
        }
        return ans;
    }
};