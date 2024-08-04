from typing import List

def find_kth_element(nums1: List[int], nums2: List[int], k: int):
    """
    This function returns the k-th element in the merged sorted array.
    The function is implemented to achieve O(log(n1 + n2)) time complexity.
    """
    len1, len2 = len(nums1), len(nums2)
    
    # Ensure nums1 is the smaller array
    if len1 > len2:
        return find_kth_element(nums2, nums1, k)
    
    # If nums1 is empty, return the k-th element in nums2
    if len1 == 0:
        return nums2[k - 1]
    
    # If k is 1, return the minimum of the first elements of both arrays
    if k == 1:
        return min(nums1[0], nums2[0])
    
    # Divide k into two parts
    i = min(len1, k // 2)
    j = min(len2, k // 2)
    
    if nums1[i - 1] > nums2[j - 1]:
        # Exclude the first j elements of nums2 and adjust k
        return find_kth_element(nums1, nums2[j:], k - j)
    else:
        # Exclude the first i elements of nums1 and adjust k
        return find_kth_element(nums1[i:], nums2, k - i)






class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        total_len = len1 + len2
        
        if total_len % 2 == 1:
            return find_kth_element(nums1, nums2, total_len // 2 + 1)
        else:
            left = find_kth_element(nums1, nums2, total_len // 2)
            right = find_kth_element(nums1, nums2, total_len // 2 + 1)
            return (left + right) / 2


if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [3,4]

    # s = find_kth_element(nums1, nums2, 10)
    # print(s)
    s = Solution().findMedianSortedArrays(nums1, nums2)
    print(s)