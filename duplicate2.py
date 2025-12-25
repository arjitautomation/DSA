class duplicate_check_set:
    def duplicate(self, nums,target):
        num_to_check={}
        for i in range(len(nums)):
            if (nums[i] in num_to_check) and i-num_to_check[nums[i]]<=target:
                return True
            else:
                num_to_check[nums[i]]=i
        return False

duplicate=duplicate_check_set();
print(duplicate.duplicate([1,2,3,1],3))    
            

    