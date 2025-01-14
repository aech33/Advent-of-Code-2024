import networkx as nx

E = []
file_path = "inputs/23.in"
with open(file_path, "r") as file:
    for line in file.readlines():
        E.append(tuple(line.strip().split("-")))

G = nx.Graph()
G.add_edges_from(E)
cliques = list(nx.enumerate_all_cliques(G))

p1 = set()
for c in cliques:
    if len(c) != 3:
        continue
    for n in c:
        if n[0] == "t":
            p1.add(tuple(c))

p2 = []
for node in max(cliques, key=len):
    p2.append(node)

print(len(p1))
print(",".join(sorted(p2)))