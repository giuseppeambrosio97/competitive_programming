#include <bits/stdc++.h>

using namespace std;

/**
 * n = s1.length(), m = s2.length()
 * Time complexity O(n*m)
 * */
// class Solution
// {
// public:
//     bool isPermutationOf(string s1, string s2)
//     {
//         if (s1.length() != s2.length())
//         {
//             return false;
//         }

//         int count[26] = {0};
//         for (int i = 0; i < s1.length(); i++)
//         {
//             count[s1[i] - 'a']++;
//             count[s2[i] - 'a']--;
//         }
//         for (int i = 0; i < 26; i++)
//         {
//             if (count[i])
//             {
//                 return false;
//             }
//         }
//         return true;
//     }
//     bool checkInclusion(string s1, string s2)
//     {
//         int ns1 = s1.length(), ns2 = s2.length();
//         for (int i = 0; i <= ns2 - ns1; i++)
//         {
//             if (isPermutationOf(s1, s2.substr(i, ns1)))
//             {
//                 return true;
//             }
//         }
//         return false;
//     }
// };

/**
 * n = s1.length(), m = s2.length()
 * Time complexity O(26(n+m))
 * */
// class Solution
// {
// public:
//     bool equal(int c1[], int c2[])
//     {
//         for (int j = 0; j < 26; j++)
//         {
//             if (c1[j] != c2[j])
//             {
//                 return false;
//             }
//         }
//         return true;
//     }

//     bool checkInclusion(string s1, string s2)
//     {
//         int ns1 = s1.length(), ns2 = s2.length();

//         if (ns1 > ns2)
//         {
//             return false;
//         }

//         int counts1[26] = {0}, counts2[26] = {0};

//         for (int i = 0; i < ns1; i++)
//         {
//             counts1[s1[i] - 'a']++;
//             counts2[s2[i] - 'a']++;
//         }

//         if (equal(counts1, counts2))
//         {
//             return true;
//         }

//         for (int i = ns1; i < ns2; i++)
//         {
//             counts2[s2[i] - 'a']++;
//             counts2[s2[i - ns1] - 'a']--;
//             if (equal(counts1, counts2))
//             {
//                 return true;
//             }
//         }

//         return false;
//     }
// };

/**
 * n = s1.length(), m = s2.length()
 * Time complexity O(n+m)
 * */
class Solution
{
public:
    bool checkInclusion(string s1, string s2)
    {
        int ns1 = s1.length(), ns2 = s2.length();

        if (ns1 > ns2)
        {
            return false;
        }

        int counts1[26] = {0}, counts2[26] = {0};

        for (int i = 0; i < ns1; i++)
        {
            counts1[s1[i] - 'a']++;
            counts2[s2[i] - 'a']++;
        }

        int matches = 0;

        for (int i = 0; i < 26; i++)
        {
            if (counts1[i] == counts2[i])
            {
                matches++;
            }
        }

        for (int i = ns1; i < ns2; i++)
        {
            if (matches == 26)
            {
                return true;
            }

            counts2[s2[i] - 'a']++;
            if (counts2[s2[i] - 'a'] == counts1[s2[i] - 'a'])
            {
                matches++;
            }
            else if (counts2[s2[i] - 'a'] - 1 == counts1[s2[i] - 'a'])
            {
                matches--;
            }

            counts2[s2[i - ns1] - 'a']--;
            if (counts2[s2[i - ns1] - 'a'] == counts1[s2[i - ns1] - 'a'])
            {
                matches++;
            }
            else if (counts2[s2[i - ns1] - 'a'] + 1 == counts1[s2[i - ns1] - 'a'])
            {
                matches--;
            }
        }

        return matches == 26;
    }
};

int main()
{
    Solution solution;
    string s1 = "adc", s2 = "dcda";

    cout << solution.checkInclusion(s1, s2) << endl;

    // int ns1 = s1.length(), ns2 = s2.length();
    // int counts1[26] = {0}, counts2[26] = {0};

    // for (int i = 0; i < ns1; i++)
    // {
    //     counts1[s1[i] - 'a']++;
    //     counts2[s2[i] - 'a']++;
    // }

    // int j = ns1;
    // counts2[s2[j] - 'a']++;
    // counts2[s2[j - ns1] - 'a']--;

    // for (int i = 0; i < 26; i++)
    // {
    //     cout << counts1[i] << ' ';
    // }
    // cout << endl;

    // for (int i = 0; i < 26; i++)
    // {
    //     cout << counts2[i] << ' ';
    // }
}