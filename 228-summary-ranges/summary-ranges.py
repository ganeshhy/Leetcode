class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:  # Handle empty list
            return []

        resu = []
        start = nums[0]  # Initialize the start of the range

        for i in range(1, len(nums)):
            # Check for non-consecutive numbers
            if nums[i] != nums[i - 1] + 1:
                # Add range or single number to result
                if start == nums[i - 1]:
                    resu.append(str(start))
                else:
                    resu.append("{}->{}".format(start, nums[i - 1]))
                start = nums[i]  # Start a new range

        # Handle the final range
        if start == nums[-1]:
            resu.append(str(start))
        else:
            resu.append("{}->{}".format(start, nums[-1]))

        return resu
