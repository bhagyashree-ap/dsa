class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def sq_dist(pt1, pt2):
            x_diff=pt1[0]-pt2[0]
            y_diff=pt1[1]-pt2[1]
            return x_diff*x_diff + y_diff*y_diff  #squared distance between 2pts

        dist=[
            sq_dist(p1,p2),
            sq_dist(p1,p3),
            sq_dist(p1,p4),
            sq_dist(p2,p3),
            sq_dist(p2,p4),
            sq_dist(p3,p4)
            ]
        
        #first 4 are sides, last 2 are diagonals
        dist.sort()
        
        #check: side length is +ve, all 4 sides are equal, both diagonals are equal
        return (dist[0]>0 and dist[0]==dist[1]==dist[2]==dist[3] and dist[4]==dist[5])