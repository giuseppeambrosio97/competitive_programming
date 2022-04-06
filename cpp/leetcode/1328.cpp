#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution
{
public:
    string breakPalindrome(string palindrome)
    {

        int n = palindrome.length();

        if (n == 1)
        {
            return "";
        }
        for (int i = 0; i < n / 2; i++)
        {
            if (palindrome[i] != 'a')
            {
                palindrome[i] = 'a';
                return palindrome;
            }
        }

        // if get there the first n/2 elements are equal to 'a'
        palindrome[n - 1] = 'b';

        return palindrome;
    }
};

int main()
{
    return 0;
}