'''
this is for fun
don't copy and paste for answer
enjoy the process and creativity
'''
def twoSumBruteForce(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j):
                    print(i,j)
                    if (nums[i] + nums[j] == target):
                        return (i,j)

test = [3,3]
twoSum(test, 6)
