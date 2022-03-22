#include <bits/stdc++.h>

using namespace std;

/**
 * Solution without using explict sorting
 * */
class Solution
{
public:
    string sortSentence(string s)
    {
        vector<string> words(10);

        int l = 0, r = 0, cnt = 0;
        while (r < s.length())
        {
            while (r < s.length() && s[r] != ' ')
            {
                r++;
            }
            string word = s.substr(l, r - l - 1);
            words[stoi(string(1, s[r - 1]))] = word;
            r++;
            l = r;
            cnt++;
        }
        string res = "";
        for (int i = 1; i <= cnt; i++)
        {
            res += words[i] + " ";
        }
        res.pop_back();
        return res;
    }
};

/**
 * Solution with explicit sorting
 * */
class Solution_srt
{
public:
    static bool cmp(string s1, string s2)
    {
        return stoi(string(1, s1.back())) < stoi(string(1, s2.back()));
    }
    vector<string> split(string s)
    {
        vector<string> words;

        int l = 0, r = 0, cnt = 0;
        while (r < s.length())
        {
            while (r < s.length() && s[r] != ' ')
            {
                r++;
            }
            words.push_back(s.substr(l, r - l));
            r++;
            l = r;
        }
        sort(words.begin(), words.end(), cmp);

        return words;
    }
    string sortSentence(string s)
    {
        string res = "";
        for (string word : split(s))
        {
            word.pop_back();
            res = res + word + " ";
        }
        res.pop_back();
        return res;
    }
};

int main()
{
    string s = "Myself2 Me1 I4 and3";
    Solution solution;
    cout << solution.sortSentence(s) << endl;
    Solution_srt solution_sort;
    cout << solution_sort.sortSentence(s);
}