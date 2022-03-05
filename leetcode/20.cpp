#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution
{
public:
    bool isValid(string s)
    {
        stack<char> sk;

        for (int i = 0; i < s.length(); i++)
        {
            char ch = s.at(i);
            if (ch == '(')
            {
                sk.push(')');
            }
            else if (ch == '[')
            {
                sk.push(']');
            }
            else if (ch == '{')
            {
                sk.push('}');
            }
            else
            {
                if (sk.size() == 0 || sk.top() != ch)
                {
                    return false;
                }
                else
                {
                    sk.pop();
                }
            }
        }
        return sk.size() == 0;
    }
};