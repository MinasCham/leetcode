class Solution(object):
    

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        min_len=sorted([len(wrd) for wrd in strs])[0]
        for i in range(min_len):
            current_char = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i]!=current_char:
                    return res
            res+=current_char
        return res
        