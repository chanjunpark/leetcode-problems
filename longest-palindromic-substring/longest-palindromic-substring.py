class Solution:
    def isPalindrome(self, string):
        for i in range(len(string)):
            if(string[i] != string[-(i+1)]):
                return False
        return True
    
    def expandWindow(self, s, L, R):
        while L>=0 and R<len(s) and s[L] == s[R]:
            L = L-1
            R = R+1
        return R-L-1
    
    def longestPalindrome(self, s: str) -> str:
        '''index_arr = []
        longest = ''
        window = 1
        flag = True
        while window < len(s):
            if flag:
                for i in range(0,len(s)-window+1):
                     if self.isPalindrome(s[i:(i+window)]):
                            longest = s[i:i+window]
                            index_arr.append([i:i+window])
            else :
                
            window = window + 1'''
        if len(s) < 1 :
            return '';
        start = 0
        end = 0
        for i in range(len(s)):
            window1 = self.expandWindow(s, i, i)
            window2 = self.expandWindow(s, i, i+1)
            window = max([window1, window2])
            if window > end - start:
                start = i - (window-1)//2
                end = i + window//2
        return s[start:(end+1)]        