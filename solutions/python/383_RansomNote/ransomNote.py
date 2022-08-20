class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        sol=""
        for i in ransomNote:
            for j in magazine:
                if j==i:
                    sol+=j
                    magazine = magazine.replace(j,'',1)
                    break
        if sol==ransomNote:
            return True
        return False