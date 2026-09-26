class Solution:
    def isValid(self, s: str) -> bool:
       h =  { ")" : "(", "}" : "{", "]" : "[" }
       sr = []
       for i in s:
            if i not in h:
                sr.append(i)
            elif i in h:
                if sr and sr[-1] == h[i]:
                    sr.pop()
                else:
                    return False
       if len(sr) > 0:
        return False
        
       return True
            
