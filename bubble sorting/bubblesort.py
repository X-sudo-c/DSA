from typing import List

nums = [5, 3, 8, 6, 2]



print(range(len(nums)))



x = range(5)

for i in x:
    print(i)

def sort(nums:List[int])-> List[int]:
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
        pass








#sort(nums)

#print(nums)