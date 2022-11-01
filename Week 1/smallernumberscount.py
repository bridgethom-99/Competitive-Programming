class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)  # creating a sorted list temporarily
        mapping = {}
        x = []
        for i in range(len(temp)):
            if temp[i] not in mapping:
                mapping[temp[i]] = i  # no of appearance
        for i in range(len(nums)):
            # returning the no of times num[i] has appeared
            x.append(mapping[nums[i]])
        return x
