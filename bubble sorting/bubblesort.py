from typing import List

nums = [5, 3, 8, 6, 2]


n = len(nums)


#bubble sort algorithm
def sort(nums):
    for i in range(n):
        for j in range (0, n - i -1):
            if nums[j] > nums[j + 1]:
                #Swap elements
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return [str(num)for num in nums]
    

#Run and print result

sorted_nums = sort(nums)

print("Sorted (as strings):", sorted_nums)
    
    




#sort(nums)

#print(nums)