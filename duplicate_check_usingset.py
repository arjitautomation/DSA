class duplicate_check_set:
    def duplicate(self, nums):
        seen=set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

duplicate=duplicate_check_set();
print(duplicate.duplicate([1,2,3,2,4]))    
            

    