class Solution(object):
    def getConcatenation(self, nums):

        phani = []
        for i in range(len(nums)):
            phani.append(nums[i])
        nums += phani
        return nums
