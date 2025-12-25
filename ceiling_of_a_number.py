class celing:
    def ceiling(self,arr,num):
        low=0
        high=len(arr)-1
        result=-1
        while(low<=high):
            mid=(low+high)//2
            if (arr[mid]==num):
                return mid
            elif(arr[mid]>num):
                high=mid-1
            else:
                low=mid+1
        return result

sol=celing()
arr=[1,2,3,4,5,6,7,8,9,10]
res=sol.ceiling(arr,9)
print(res)

       
