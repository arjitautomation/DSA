class Solution:
    @staticmethod
    def binary(arr,target):
        l=len(arr)
        low=0
        high=l-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid] == target:
                return mid
            elif target > arr[mid]:
                low=mid+1
            else:
                high =mid -1
        return -1

arr=[1,2,3,4,5,6,7,8,9,10]
Solution.binary(arr,5)    
