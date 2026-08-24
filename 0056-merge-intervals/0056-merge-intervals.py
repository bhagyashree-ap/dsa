class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res=[intervals[0]]  #first interval

        for start, end in intervals[1:]:
            if start<=res[-1][1]:   #overlap
                res[-1][1]=max(res[-1][1], end)
            
            else:       #separate
                res.append([start,end])
        
        return res