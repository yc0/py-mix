class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "({},{})".format(self.x,self.y)
class Solution:
    """
    Andrew's monotone chain convex hull algorithm constructs the convex hull of 
    a set of 2-dimensional points in O(nlogn) time.

    It does so by first sorting the points lexicographically (first by x-coordinate, and in case of a tie, by y-coordinate), 
    and then constructing upper and lower hulls of the points in O(n) time.

    An upper hull is the part of the convex hull, which is visible from the above. 
    It runs from its rightmost point to the leftmost point in counterclockwise order. 
    Lower hull is the remaining part of the convex hull.


    refer : https://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain
    """
    def monotone(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        points =  [Point(x[0],x[1]) for x in points]

        if not points or len(points) < 3:
            return points

        points = sorted(set(points), key=lambda p: (p.x,p.y))
        lower, upper = [],[]
        for p in points:
            while len(lower) > 1 and self.ccw(lower[-2],lower[-1],p) < 0:
                lower.pop()
            lower.append(p)
        
        for p in reversed(points):
            while len(upper) > 1 and self.ccw(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)
        return list(set(lower[:-1]+upper[:-1]))
    """
    Graham's scan, time complexity (nlogn)
    ref:https://zh.wikipedia.org/wiki/葛立恆掃描法
    # 当ccw函数的值为正的时候，三个点为“左转”（counter-clockwise turn），如果是负的，则是“右转”的，而如果
    # 为0，则三点共线，因为ccw函数计算了由p1,p2,p3三个点围成的三角形的有向面积
    function ccw(p1, p2, p3):
       return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)
    """
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """

        points =  [Point(x[0],x[1]) for x in points]
        # could be O(n) for only finding minimum x and minium y
        # But I sort the data for convenience purpose
        start = min(points, key=lambda p: (p.x,p.y)) 
        points.pop(points.index(start))

        print(start)
        
        points.sort(key=lambda p: (self.slope(start,p),-p.y,p.x))
        # _points = sorted(points[1:],key=lambda p: self.dot(P,p))
        # _points = sorted(points[1:],key=lambda p: self.slope(P,p),, reverse= True)
        # # _points.reverse()
        # # print(P,_points, _points2)
        # S = [P,_points[-1]]
        S = [start]
        for p in points:
            S.append(p)
            while len(S) > 2 and self.ccw(S[-3],S[-2],S[-1]) < 0:
                S.pop(-2)
        return S
        # for i in range(len(_points)-2, -1, -1):
        #     while len(S) > 1 and self.ccw(S[-2],S[-1],_points[i]) < 0 : #exclude collinear for this problem
        #         S.pop()
        #     S.append(_points[i])
        # return S

    def ccw(self, o, a, b): # cross product
        return (a.x-o.x)*(b.y-o.y) - (b.x-o.x)*(a.y-o.y)
    def dot(self, a, b): # dot product, here, we need only length btw a and b
        return (a.x-b.x)**2+(a.y-b.y)**2
    def slope(self,a,b): # slope
        return float(b.y-a.y)/(b.x-a.x) if b.x != a.x else float('inf')
    
"""
Time Limit Exceed
"""    
class Solution_TLE:
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        """fuck !!! what's Point structure like @@ """
        points =  [Point(x[0],x[1]) for x in points]
        print(points)
        if not points or len(points) < 3:
            return points
        visited= set()
        for p in points:
            if p in visited:
                continue
            for q in points:
                if q == p or p in visited:
                    continue
                    
                S, C = self.linear(p,q)
                direction = 0 # -1 means y<ax+b, 0 y=ax+b, 1 y>ax+b
                validate, temp = True, set()
                for s in points:
                    if s != q and s!= p:
                        if S == float('inf'): # perpendicular
                            if s.x == C:
                                temp.add(s)
                            elif direction == 0:
                                if s.x < C:
                                    direction = -1
                                else:
                                    direction = 1
                            elif (direction == 1 and s.x < C) or (direction == -1 and s.x > C):
                                validate = False
                                break
                        elif S == 0:
                            if s.y == C:
                                temp.add(s)
                            elif direction == 0:
                                if s.y < C:
                                    direction = -1
                                else:
                                    direction = 1
                            elif (direction == 1 and s.y < C) or (direction == -1 and s.y > C):
                                validate = False
                                break

                        else:
                            if s.y == s.x*S+C:
                                temp.add(s)
                            elif direction == 0:
                                if s.y > s.x*S+C:
                                    direction = 1
                                else:
                                    direction = -1                  
                            elif (direction == 1 and s.y < s.x*S+C) or (direction == -1 and s.y > s.x*S+C):
                                validate = False
                                print(p,q,s)
                                break
                if validate:
                    visited.add(p)
                    visited.add(q)
                    visited |= temp
                else:
                    print(p,q,"passed")
        return sorted(list(visited),key=lambda p: (p.x,p.y))
        
    def linear(self,A,B):
        """
        y = ax+b
        A[1] = a*A[0]+b
        B[1] = a*B[0]+b
        
        A[1]-B[1] = a*(A[0]-B[0])
        a = (A[1]-B[1])/(A[0]-B[0])
        b = A[1]-a*A[0]
        
        return a,b
        """
        print(A,B)
        if A.x == B.x:
            return float('inf'),A.x # x=c

        if A.y == B.y:
            return 0, A.y

        slope = (A.y-B.y)/(A.x-B.x)
        C = A.y-slope*A.x
        return slope,C

if __name__ == "__main__":
    s = Solution()
    print(s.outerTrees([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]))
    #[[1,1],[2,0],[4,2],[3,3],[2,4]]
    print(s.outerTrees([[1,2],[2,2],[4,2]]))
    print(s.monotone([[1,2],[2,2],[4,2]]))
    print(s.outerTrees([[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]))
    print(s.monotone([[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]))
    #[[0,3],[1,2],[2,1],[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4]]