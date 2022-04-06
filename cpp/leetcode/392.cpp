#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

/**********
 * sn = s.length(), tn = t.length
 * This solution for each i = 0...tn-sn check if string s is a subsequence starting at t[i] of t[i]..t[tn-1].
 * Where with starting at t[i] we means that t[i] == s[i]
 * 
 * Time Complexity: O(tn*sn)
 * 
 * 
 * ********/
class Solution
{
public:
    int find_first_of(string t, int j, char ch)
    {
        for (int i = j; i < t.length(); i++)
        {
            if (t[i] == ch)
            {
                return i;
            }
        }
        return -1;
    }

    bool isSubsequence_starting_at_i(int i, string s, string t)
    {
        int k = i;
        for (int j = 0; j < s.length(); j++)
        {
            k = find_first_of(t, k, s.at(j));
            if (k == -1)
            {
                return false;
            }
            k++;
        }
        return true;
    }

    bool isSubsequence(string s, string t)
    {
        int sn = s.length(), tn = t.length();
        for (int i = 0; i <= tn - sn; i++)
        {
            if (isSubsequence_starting_at_i(i, s, t))
            {
                return true;
            }
        }
        return false;
    }
};

class Solution
{
public:
    int find_first_of(string t, int j, char ch)
    {
        for (int i = j; i < t.length(); i++)
        {
            if (t[i] == ch)
            {
                return i + 1;
            }
        }
        return -1;
    }
    bool isSubsequence(string s, string t)
    {
        int sn = s.length(), tn = t.length(), k = 0;
        for (int i = 0; i < sn; i++)
        {
            k = find_first_of(t, k, s.at(i));
            if (k == -1)
            {
                return false;
            }
        }
        return true;
    }
};

class Solution
{
public:
    bool isSubsequence(string s, string t)
    {
        int sn = s.length(), tn = t.length(), j = 0;
        for (int i = 0; i < sn; i++)
        {
            while (j < tn && s.at(i) != t.at(j))
            {
                j++;
            }
            if (j == tn)
            {
                return false;
            }
            j++;
        }
        return true;
    }
};

class Solution
{
public:
    bool isSubsequence(string s, string t)
    {
        int sn = s.length(), tn = t.length();
        int i = 0, j = 0;

        while (i < sn && j < tn)
        {
            if (s.at(i) == t.at(j))
            {
                i++;
            }
            j++;
        }
        return i == sn;
    }
};

int main()
{
    Solution s;
    cout << s.isSubsequence("aaaaaa", "bbaaaa") << "\n";
}