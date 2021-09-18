class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m+n,0,-1):
            if len(nums2) == 0:
                nums1[i-1] = nums1[m-1]
                m = m-1
            elif m-1 < 0 :
                nums1[i-1] = nums2.pop()
            else:
                if nums1[m-1] <= nums2[-1]:
                    nums1[i-1] = nums2.pop()
                else:
                    nums1[i-1] = nums1[m-1]
                    m = m-1
            print(i,nums1)
                

        