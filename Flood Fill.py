#TC - O(N)
#SC - O(N)
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color:
            return image
        
        self.image = image
        self.m = len(image)
        self.n = len(image[0])
        self.oldcolor = image[sr][sc]
        self.color = color
        self.dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        self.dfs(sr,sc)
        return self.image
        
        
    def dfs(self,sr,sc):
        if sr<0 or sr>=self.m or sc<0 or sc>=self.n or self.image[sr][sc] != self.oldcolor:
            return 
        
        self.image[sr][sc] = self.color
        for dx,dy in self.dirs:
            nr = sr+dx
            nc = sc+dy
            self.dfs(nr,nc)