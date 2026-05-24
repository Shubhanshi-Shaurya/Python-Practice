#SEARCHING AND SORTING 


def sortArray(self, nums):
        #BUBBLE SORT
        n=len(nums)
        
        for i in range (n):
            for j in range (n-i-1):
                if nums[j]>nums[j+1]:
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp
        return nums

#INSERTION SORT 
def sortArray(self, nums):
        n=len(nums)

        for i in range (1,n):
            key=nums[i]
            j=i-1
            while j>=0 and nums[j]>key:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key

        return nums

#SELECTION SORT 
def sortArray(self, nums):
        n=len(nums)

        for i in range(n):
            mn=nums[i]
            idx=i
            for j in range(i+1,n):
                if nums[j]<mn:
                    mn=nums[j]
                    idx=j

            temp=nums[i]
            nums[i]=nums[idx]
            nums[idx]=temp

        return nums

#MERGE SORT 



