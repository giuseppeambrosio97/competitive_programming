#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution
{
public:
    int counts_combination_sum_i(vector<int> &a, int i, int t){
        if (t == 0)
        {
            return 1;
        }
        
        int sum = 0;
        for (int j = i; j < a.size(); j++)
        {
            if (a[j] <= t){
                sum += counts_combination_sum_i(a, j, t - a[j]);
            }
        }

        return sum;
    }


    /**
     * this function counts the number of possible solutions to the problem!
     * */
    int counts_combinationSum(vector<int> &a, int t)
    {
        return counts_combination_sum_i(a, 0, t);
    }

    vector<vector<int>> combinationSum(vector<int> &a, int t)
    {
        
    }
};

int main()
{
    Solution solution;
    vector<int> v({2});

    cout << solution.counts_combinationSum(v, 1) << "\n";

}