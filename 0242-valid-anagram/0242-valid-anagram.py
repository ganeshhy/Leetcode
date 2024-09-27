class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        st=[]
        pt=[]
        st.extend(s)
        pt.extend(t)
        st.sort()
        pt.sort()
        if st==pt:
            return True
        return False
        