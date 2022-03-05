#include <bits/stdc++.h>

using namespace std;

typedef long long ll;


/****
 * This solution use two index i and j.
 * The index i counts the number of elements that are different from val.
 * The index j is used to iterate over nums.
 *      When we find an element that is different from val we store it in the position i, which we recall
 *      keeps track of the number of elements that are different from val. After that we should increase i
 *      by one, because the new value stored is a new value different from val.
 * 
 * Time complexity is O(n)
 * Space complexity is O(1)
 * 
 * The "problem" of this solution is that in there are low number of elements to delete we will uncessary copy operation.
 * nums=[1,2,3,4,5] and val = 6, the operation nums[i++] = nums[j] is always uncessary. 
 * ***/
class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        // With I we count the number of element that are different from val
        int i = 0;
        for (int j = 0; j < nums.size(); j++)
        {
            if (nums[j] != val)
            {
                //IF nums[j] is different from val then I keep it otherwise I simply ignore.
                nums[i++] = nums[j];
            }
        }
        return i;
    }
};

/***************
 * This solution leverage the fact that we can change the order on the elements in the array.
 * 
 * So when we encounter an element different from val we do nothing. 
 * If we encounter an element equal to val we take an element from the end of the array.
 * 
 * This solution is more efficient respect the previous solution, but it doesn't check
 * if the element taken from the end of the array is different from val or not.
 * It takes the element and swap it with the current element and in the next iteration it try to swap it
 * if before it was a bad element.
 * 
 * 
 * */
class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        int l = 0, n = nums.size();

        while (l < n)
        {
            if (nums[l] == val)
            {
                nums[l] = nums[n - 1];
                n--;
            }
            else
            {
                l++;
            }
        }
        return n;
    }
};


/***
 * This solution is an improvement of the previous one.
 * When it takes an element from the end of the array it doens't take bad element but 
 * iterate (backwards) until it find a good element available (if there are any) 
 * */
class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        int l = 0, n = nums.size();

        while (l < n)
        {
            if (nums[l] == val)
            {
                // n-1 != l to check if the current nums[l] is not the same as
                // the one we want to swap with 
                while (nums[n - 1] == val && n - 1 != l)
                {
                    n--;
                }
                nums[l] = nums[n - 1];
                n--;
            }
            l++;
        }
        return n;
    }
};