typedef long long ll;

class Solution
{
public:
    /**
     * Given a number num return true if exist a s.t a^2 = num and false otherwise.
     * 
     * */
    bool isPerfectSquare(int num)
    {
        ll l = 1, r = num;
        while (l <= r)
        {
            ll a = (l + r) / 2;
            if (a * a == num)
            {
                return true;
            }
            if (a * a < num)
            {
                //a+1,a+2,...,r
                l = a + 1;
            }
            else
            {
                //l,l+1,...,a-1
                r = a - 1;
            }
        }
        return false;
    }
};
