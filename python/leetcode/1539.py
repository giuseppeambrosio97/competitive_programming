from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        T(n,k) = O(n + 1000)
        S(n,k) = O(1000)

        def findKthPositive(self, arr: List[int], k: int) -> int:
            missing = []
            _n = len(arr)
            for idx in range(_n + 1):
                if idx == 0:
                    missing += list(range(1, arr[idx]))
                elif idx == _n:
                    missing += list(range(arr[-1] + 1, 1001))
                else:
                    missing += list(range(arr[idx-1]+1, arr[idx]))
            return missing[k-1] if len(missing) >= k else 1000 + (k - len(missing))

        T(n,k) = O(arr[-1]) = O(1000)
        S(n,k) = O(1) 
        def findKthPositive(self, arr: List[int], k: int) -> int:    
            n, i, j = len(arr), 0, 1 ## j is the current element that we want to check if it is missing or not
            cnt = 0 # count the missing elements

            ## this loop iterates at most arr[-1] times
            while i < n:
                if arr[i] != j:
                    cnt += 1
                    if cnt == k:
                        return j
                else:
                    i += 1
                j += 1

            return arr[-1] + (k - cnt)

        using binary search we can have
        T(n, k) = O(log(n)) = O(log1000)
        S(n, k) = O(1)
        """
        def missing_before_i(a: List[int], i):
            return a[i] - i - 1

        # check edge case in which the missing k-th number is after the last element of the array
        n = len(arr)
        missing_before_last = missing_before_i(arr, n-1)
        if missing_before_last < k:
            return arr[-1] + k - missing_before_last

        ## now we know that the missing k-th number is smaller than arr[-1] so we can do binary search
        ## to find the smallest i for which missing_before_i(arr, i) >= k 
        l, r = 0, n - 1
        while l <= r:
            m = (r + l) // 2
            missing_before_m = missing_before_i(arr,m)
            if missing_before_m >= k:
                if m == 0:
                    return k
                missing_before_m_1 = missing_before_i(arr, m-1)
                if missing_before_m_1 < k:
                    return arr[m-1] + (k-missing_before_m_1)  
                r = m - 1
            else:
                l = m + 1



if __name__ == '__main__':
    arr = [2]
    k = 1
    s = Solution().findKthPositive(arr, k)
    print(s)