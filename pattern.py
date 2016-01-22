class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        line = str.split()
        if len(line) != len(pattern):
            return False
        print "length of line", len(line)
        print 'length of pattern', len(pattern)
    	for i in range(0,len(pattern)-1):
    		for j in range(1, len(pattern)):
    			print "char in parttern", i ,pattern[i], "char in patter", j , pattern[j]
    			print "char in str", i ,line[i], "char in str", j , line[j]
    			if pattern[i] == pattern[j] and line[i] != line[j]:
    				return False
    			elif pattern[i] != pattern[j] and line[i] == line[j]:
    				return False
    		
	return True

solution = Solution()
print solution.wordPattern("abbabcdd", "dog cat cat dog cat fish mouse mous")