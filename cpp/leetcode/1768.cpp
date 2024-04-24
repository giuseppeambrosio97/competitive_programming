#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    string mergeAlternately(string word1, string word2)
    {
        int n1 = word1.length();
        int n2 = word2.length();
        int min_n = -1;
        string extra = "";
        if (n1 > n2)
        {
            min_n = n2;
            extra = word1.substr(n2, n1 - n2);
        }
        else
        {
            min_n = n1;
            extra = word2.substr(n1, n2 - n1);
        }

        string merged = "";
        for (int i = 0; i < (min_n*2); i+=2)
        {
            merged += word1[i / 2];
            merged += word2[(i + 1) / 2];
        }

        return merged + extra;
    }
};

int main()
{
    Solution solution;
    string word1 = "abc";
    string word2 = "pqrcccc";
    string merged = solution.mergeAlternately(word1, word2);
    cout << "Merged string: " << merged << endl;
    return 0;
}
