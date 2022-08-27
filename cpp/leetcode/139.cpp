#include <bits/stdc++.h>

using namespace std;

/**
 * s0,...,s_{n-1} | wordDict
 *
 * s[i,j] = s_i,...,s_j
 *
 * d[i] = the solution for the substring s0,...,s_{i}; for i = 0,...,n-1
 *
 * d[0] = false     - if s0 is not contained in wordDict
 *      = true      - if s0 is contained in wordDict
 *
 * d[i] = OR(d[i-j] and s[i-j,i]) for j=0,...,i
 *
 * */
class Solution
{
public:
    bool find_word_dict(string s, vector<string> &wordDict)
    {
        return find(wordDict.begin(), wordDict.end(), s) != wordDict.end();
    }

    bool wordBreak(string s, vector<string> &wordDict)
    {
        s = " " + s;
        int n = s.length();
        vector<bool> d(n, false);
        d[0] = true;

        for (int i = 1; i < n; i++)
        {
            for (int j = 0; j < i; j++)
            {
                bool tmp = d[j] && find_word_dict(s.substr(j + 1, i - j), wordDict);
                d[i] = d[i] || tmp;
            }
        }

        return d[n - 1];
    }
};

int main()
{
    vector<string> wordDict({"apple", "pen"});
    string s = "applepenapple";

    Solution sol;

    cout << sol.wordBreak(s, wordDict) << "\n";
    // cout << s.substr(n,n+1)  << "\n";
    // cout << sol.find_word_dict(s.substr(n-1,n), wordDict) << '\n';

    return 0;
}