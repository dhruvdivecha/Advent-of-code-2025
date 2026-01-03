from collections import defaultdict

def load_input():
    with open('day8/input.txt') as f:
        data = [line.rstrip() for line in f.readlines()]
    return data

def parse(data):
    data = [line.split(',') for line in data]
    data = [(int(x), int(y), int(z)) for x,y,z in data]
    return data

def get_distances(nodes):
    distances = []
    for i in range(len(nodes) - 1):
        for j in range(i + 1, len(nodes)):
            x1, y1, z1 = nodes[i]
            x2, y2, z2 = nodes[j]
            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
            distances.append((distance, i, j))
    return distances 
        
def find(parents, i):
    if parents[i] == i:
        return i
    
    parents[i] = find(parents, parents[i])
    return parents[i]


def union(parents, i, j):
    pi = find(parents, i)

    pj = find(parents, j)

    parents[pj] = pi


def part1(data):
    nodes = parse(data)
    parents = {i: i for i in range(len(nodes))}

    distances = get_distances(nodes)
    distances.sort()

    for pair in range(1000):
        _, i, j = distances[pair]

        if find(parents, i) == find(parents, j):
            continue

        union(parents, i, j)
    
    sizes = defaultdict(int)
    
    for node in parents.values():
        root = find(parents, node)
        sizes[root] += 1
            
    ans = 1
    for s in sorted(sizes.values(), reverse=True)[:3]:
        ans *= s

    return ans

def part2(data):
    nodes = parse(data)
    parents = {i:i for i in range(len(nodes))}

    distances = get_distances(nodes)

    distances.sort()

    for _,i,j in distances:
        if find(parents, i) == find(parents, j):
            continue

        union(parents, i, j)

        if all(find(parents, 0) == find(parents, i) for i in range(len(nodes))):
            break

    x1,_,_ = nodes[i]
    x2,_,_ = nodes[j]

    return x1 * x2

    

if __name__ == "__main__":
    data = load_input()
    result = part1(data)
    print(result)
    result2 = part2(data)
    print(result2)