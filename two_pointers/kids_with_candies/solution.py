class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        i=0
        ret=[]
        while i<len(candies):
            if candies[i]+extraCandies>=m:
                ret.append(True) 
            else :
                ret.append(False)
            i+=1
        return ret