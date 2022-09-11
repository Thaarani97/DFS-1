#TC - O(V+E)
#SC - O(v+E)
class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        self.critical_conn = []
        self.arrival_time = [0]*n
        self.minimum_time = [0]*n
        self.visited = [False] *n
        self.adj = [[] for i in range(n)]
        for i,j in connections:
            self.adj[i].append(j)
            self.adj[j].append(i)
        
        self.dfs(0,-1,-1)
        return self.critical_conn
    
    def dfs(self,node,parent,time):
        self.visited[node] = True
        time+=1
        self.arrival_time[node] = time
        self.minimum_time[node] = time
        for nchild in self.adj[node]:
            if nchild != parent:
                if not self.visited[nchild]:
                    self.dfs(nchild,node,time)
                    self.minimum_time[node] = min(self.minimum_time[node],self.minimum_time[nchild])
                    if self.minimum_time[nchild] > self.arrival_time[node]:
                        self.critical_conn.append([nchild,node])
                else:
                    self.minimum_time[node] = min(self.minimum_time[node],self.minimum_time[nchild])
    
                    