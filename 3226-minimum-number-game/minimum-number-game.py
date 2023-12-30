class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        a=[]
        while (len(nums)/2):
            if len(nums)==1:
                break
            mi=min(nums)
            nums.remove(mi)
            m=min(nums)
            nums.remove(m)
            a.append(m)
            a.append(mi)
        return a
            
            
        
        
        
        