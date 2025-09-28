class Solution:
    @staticmethod
    def binary_search(arr,target):
        high=len(arr)-1
        low=0
        while (low<=high):
            mid = (high+low)//2
            if arr[mid]==target:
                return mid
            elif arr[mid] >target:
                high=mid-1
            else: 
                low=mid+1
        return -1


arr=[1,2,3,4,5,6,7]
print(Solution.binary_search(arr,5))            

