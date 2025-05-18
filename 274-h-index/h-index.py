class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h = 0
        n = len(citations)
        for i in range(n):
            if citations[i] >= i + 1:
                h = i + 1
            else:
                break
        return h
        