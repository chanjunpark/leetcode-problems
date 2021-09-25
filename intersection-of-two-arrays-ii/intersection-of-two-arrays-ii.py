class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            longer = nums1
            shorter = nums2
        else :
            longer = nums2
            shorter = nums1
        
        intersection = []
        
        for values in shorter:
            if values in longer:
                intersection.append(values)
                longer.remove(values)
        
        return intersection
    
        