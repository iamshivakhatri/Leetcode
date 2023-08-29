class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        tdict = {}
        sdict = {}

        for c in t:
            tdict[c] = tdict.get(c, 0) + 1

        have, need = 0, len(tdict)
        left, right = 0, 0
        res = [-1, -1]
        resLen = float('inf')
        
        for c, a in enumerate(s):
            sdict[a] = sdict.get(a, 0) + 1
            if a in tdict and sdict[a] == tdict[a]:
                have += 1

            #if the given window has all the values contained in t
            while have == need:
                if (right - left + 1) < resLen:
                    resLen = right - left + 1
                    res = [left , right]

                #Pop the element from left
                sdict[s[left]] -= 1

                #after poping the element checking whether deleted element was in tdict
                if s[left] in tdict and  sdict[s[left]] < tdict[s[left]]:
                    have -= 1

                left += 1
            right += 1

        left, right = res

        return s[left: right + 1 ] if res != [-1, -1] else ""





        