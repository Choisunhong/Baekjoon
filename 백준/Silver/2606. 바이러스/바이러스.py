import sys
input = sys.stdin.readline

def find_infected_computers():
    num_computers = int(input().strip())
    num_pairs = int(input().strip())


    connections = {i: set() for i in range(1, num_computers + 1)}


    for _ in range(num_pairs):
        u, v = map(int, input().strip().split())
        connections[u].add(v)
        connections[v].add(u)

    infected = set()  
    to_visit = set([1]) 

    while to_visit:
        computer = to_visit.pop()  
        if computer not in infected: 
            infected.add(computer)  
            to_visit.update(connections[computer]) 

    return len(infected) - 1

print(find_infected_computers())
