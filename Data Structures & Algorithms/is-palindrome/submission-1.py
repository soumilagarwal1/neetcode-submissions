class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(s)
        newstr = []
        reverse1 = []
        for i in range(len(s)):
            if s[i].isalnum():
                newstr.append(s[i])
        
        for i in range(len(newstr)):
            if newstr[i].isalnum():
                reverse1.append(newstr[i])

        reverse2 = ["" for i in range(len(reverse1))]
        for i in range(len(reverse1)):
            reverse2[-i-1] = reverse1[i]
            
        
        print(reverse2)
        if reverse2 == newstr:
            return True
        else:
            return False

            
        