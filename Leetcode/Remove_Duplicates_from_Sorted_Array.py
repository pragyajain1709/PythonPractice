class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,len(nums)-1):
            if (nums[i]==nums[i+1]):
                nums[i]='delete'
        
    
        while 'delete' in nums:
            nums.remove('delete')
            
            
        return len(nums)