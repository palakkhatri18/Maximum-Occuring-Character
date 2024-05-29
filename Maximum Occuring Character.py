from collections import Counter
class Solution:
    
    #Function to find the maximum occurring character in a string.
    def getMaxOccurringChar(self,s):
        #code here
        string = Counter(s)
        
        maxi = max(string.values())
        
        box = [char for char, freq in string.items() if freq == maxi]
        
        return min(box)
            