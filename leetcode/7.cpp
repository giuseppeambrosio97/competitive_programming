#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution {
public:
    int reverse(int x) {
        int rev = 0;
        int m = 1;
        while( x % 10 != x){
            rev += ((x%10)*m);
            m *= 10;
            rev /= 10;
        }
        return rev;
    }
};