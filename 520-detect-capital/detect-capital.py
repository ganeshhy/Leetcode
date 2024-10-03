class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.upper()==word:
            return True
        if word.lower()==word:
            return True
        if word.capitalize()==word:
            return True
        return False
        