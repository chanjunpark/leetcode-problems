class Solution:
    def isPalindrome(self, x: int) -> bool:
        st = []
        answer = False
        if(x<0):
            return False;
        else:
            origin = x
            while x>0:
                st.append(x%10)
                x = x//10
            print(st)
            for i in range(len(st)):
                if(st.pop() != origin%10):
                    return False;
                else:
                    origin = origin//10
            return True;