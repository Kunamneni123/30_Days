class Solution(object):
    def moveZeroes(self, nums):

        mani = []
        while 0 in nums:
            nums.remove(0)
            mani.append(0)
        nums += mani
        return nums
