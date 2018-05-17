import networkx as nx
from collections import deque
def BFS_visit(i,G=nx.Graph(),visit_time=[],pre=[]):
    global time
    visit_list=deque()
    visit_list.append(i)
    while visit_list:
        visit=visit_list.popleft()
        print(visit)
        time=time+1
        visit_time[visit-1]=time
        for node in G:
            if G.has_edge(visit,node) and visit_time[node-1]==-1 and node not in visit_list:
                visit_list.append(node)
                pre[node-1]=visit

def BFS(G=nx.Graph()):
    pre=[]
    visit_time=[]
    i=1
    components=0
    while i<=G.number_of_nodes():
        pre.append(-1)
        visit_time.append(-1)
        i=i+1
    for node in G.nodes():
        if pre[node-1]==-1:
            BFS_visit(node,G,visit_time,pre)
            components=components+1
    print ('components',components)

time=0
G=nx.Graph()
G.add_edges_from([(1,2),(1,3),(2,4),(2,5),(3,6),(4,8),(5,8),(3,7)])
#G.add_edges_from([(0,4),(1,0),(1,2),(2,3),(2,0),(3,4)])
BFS(G)
