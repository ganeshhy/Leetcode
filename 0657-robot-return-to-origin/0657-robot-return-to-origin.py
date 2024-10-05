class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        lr=0
        ud=0
        for i in moves:
            if i=='U':
                ud+=1
            elif i=="D":
                ud-=1
            elif i=="L":
                lr+=1
            elif i=="R":
                lr-=1
        if lr==0 and ud==0:
            return True
        return False
        
        