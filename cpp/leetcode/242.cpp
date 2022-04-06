#include <bits/stdc++.h>

using namespace std;

/*******
 * This solution uses the assumption that s and t have only lowecase english letters
 * Time complexity O(n)
 * Space complexity O(26)
 * */
// class Solution
// {
// public:
//     bool isAnagram(string s, string t)
//     {
//         if (s.length() != t.length())
//         {
//             return false;
//         }
//         int count[26] = {0};

//         for (int i = 0; i < s.length(); i++)
//         {
//             count[s[i] - 'a']++;
//             count[t[i] - 'a']--;
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
// };

/**
 * This solution doesn't use the assumption that s and t have only lowecase english letters.
 * The logic is essentially the same but this solution use an unordered_map instead of an array.
 * Time complexity O(n)
 * Space complexity O(n)
 * */
// class Solution
// {
// public:
//     bool isAnagram(string s, string t)
//     {
//         if (s.length() != t.length())
//         {
//             return false;
//         }
//         unordered_map<char, int> count;

//         for (int i = 0; i < s.length(); i++)
//         {
//             count[s[i]]++;
//             count[t[i]]--;
//         }

//         for (auto &it : count)
//         {
//             if (it.second)
//             {
//                 return false;
//             }
//         }

//         return true;
//     }
// };

/**
 * Space complexity O(1)
 * Time complexity O(nlogn)
 * */
class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        if (s.length() != t.length())
        {
            return false;
        }
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        return s.compare(t) == 0;
    }
};

int main()
{
    Solution solution;
    cout << solution.isAnagram("rat", "tar") << endl;
}