class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = []
        w = []
        b = []

        for i in range(len(nums)):
            if nums[i] == 0:
                r.append(0)
            if nums[i] == 1:
                w.append(1)
            if nums[i] == 2:
                b.append(2)

        nums.clear()  # To clear current nums list
       #The extend method appends lists
        nums.extend(r)
        nums.extend(w)
        nums.extend(b)
