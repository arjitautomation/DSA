class check_duplicate:
    def duplicate(self,nums):
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                return True
        return False
            
duplicate=check_duplicate();
print(duplicate.duplicate([1,2,3,2,4]))

