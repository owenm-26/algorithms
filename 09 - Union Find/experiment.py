from heapdict import heapdict 
import math
import random
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
from bisect import bisect_left, bisect_right

class Node:
    def __init__(self, id: int):
        self.size = 1
        self.id = id
    def __repr__(self):
        return(f"{self.id}")

class UnionFind:
    def __init__(self, n:int):
        self.reps = {}
        for i in range(1,n+1):
            node = Node(id=i)
            self.reps[node] = node
        self.keys = list(self.reps.keys())

    def findPathCompression(self, u: Node) -> Node:
        """Finds topmost representative and compresses the path"""
        x = u
        while self.reps[x] != x:
            self.reps[x] = self.reps[self.reps[x]]
            x = self.reps[x]
        return x

    def unionUpdate(self, u: Node, v: Node, minHeap: heapdict, maxComp: list, minComp:list):
        """Combines two nodes components and finds the min/max component size"""
        componentU = self.findPathCompression(u)
        componentV = self.findPathCompression(v)

        if componentU != componentV:
            smaller = componentU if componentU.size < componentV.size else componentV
            larger = componentV if smaller == componentU else componentU

            # delete stale entries
            del minHeap[componentU]
            del minHeap[componentV]

            self.reps[smaller] = larger
            larger.size = larger.size + smaller.size

            # Add merged component
            minHeap[larger] = larger.size

            maxComp.append(max(maxComp[-1], larger.size))
        else:
            maxComp.append(maxComp[-1])
        
        minComp.append(minHeap.peekitem()[1])

    def addRandomEdge(self,E:set) -> tuple:
        """Adds a random connection that doesn't already exist"""

        # Choose a random key from the list
        u = random.choice(self.keys)
        v = random.choice(self.keys)
        while u == v or (u,v) in E or (v,u) in E:
            u = random.choice(self.keys)
            v = random.choice(self.keys)
        
        E.add((u,v))
        return (u,v)

def componentSizes(n:int):
    """Returns a list of the smallest and largest component sizes at each timestamp"""
    limit = 1/2 * math.comb(n, 2)
    E = set()
    minComp, maxComp = [1], [1]

    UF = UnionFind(n=n)
    minHeap = heapdict({node: 1 for node in UF.reps})

    t=1
    while(t < limit and maxComp[-1] != n):
        u,v = UF.addRandomEdge(E=E)
        UF.unionUpdate(u=u, v=v, minHeap=minHeap, minComp=minComp, maxComp=maxComp)
        t+=1
    
    return maxComp, minComp

# ########################
def unit_evaluation_experiment(n_vals: list):
    
    results = defaultdict(list)

    for n in n_vals:
        for _ in range(20):
            results[n].append((componentSizes(n)))
    
    return results

def extract_metrics(data:list, n:int):
    max_runs = [run[0] for run in data]
    min_runs = [run[1] for run in data]

    t_big, t_connect, t_no_iso, t_diff = [], [], [], []

    for i in range(len(max_runs)):

        # find t_big
        t_big.append(bisect_left(max_runs[i], n//2))

        # find t_connect
        t_connect.append(len(max_runs[i]))

        # find t_no_iso
        t_no_iso.append(bisect_right(min_runs[i], 1))
    
    # calculate t_diff
    for i in range(len(t_connect)):
        t_diff.append(t_connect[i] - t_no_iso[i])
    
    return t_big, t_connect, t_no_iso, t_diff

def plot_histogram(t_big: list, t_connect: list, t_no_iso: list, t_diff:list, n:int):
    # Normalize by n
    t_big_norm = [t / n for t in t_big]
    t_connect_norm = [t / n for t in t_connect]
    t_no_iso_norm = [t / n for t in t_no_iso]
    t_diff_norm = [t/n for t in t_diff]

    metrics = {
        "t_big / n": t_big_norm,
        "t_connect / n": t_connect_norm,
        "t_no_iso / n": t_no_iso_norm,
        # "t_diff_norm / n": t_diff_norm
    }

    plt.figure(figsize=(12, 5))

    # Plot each metric side by side
    for i, (name, values) in enumerate(metrics.items(), start=1):
        plt.subplot(1, 3, i)
        plt.hist(values, bins=10, edgecolor='black', alpha=0.7)
        plt.title(f"{name} distribution (n={n})")
        plt.xlabel("Fraction of nodes")
        plt.ylabel("Frequency")
        plt.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()

def plot_averages(data:list, n:int):
    """Plots the average minComp and maxComp sizes"""
    # Separate all maxComp and minComp runs
    max_runs = [run[0] for run in data]
    min_runs = [run[1] for run in data]

    # Find longest run length
    max_len = max(len(r) for r in max_runs)

    # Pad all runs to same length (using last value)
    def pad_run(run, length):
        if len(run) < length:
            run = run + [run[-1]] * (length - len(run))
        return run

    max_runs = np.array([pad_run(r, max_len) for r in max_runs])
    min_runs = np.array([pad_run(r, max_len) for r in min_runs])

    # Compute average across runs
    avg_max = np.mean(max_runs, axis=0)
    avg_min = np.mean(min_runs, axis=0)

    # Time steps
    t = np.arange(max_len)

    # Plot
    plt.figure(figsize=(8,5))
    plt.plot(t, avg_max, label='Average maxComp', linewidth=2)
    plt.plot(t, avg_min, label='Average minComp', linewidth=2)
    plt.title(f'Average Component Sizes over Time (n={n})')
    plt.xlabel('t (time step / number of edges added)')
    plt.ylabel('Component size')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    n_vals = [500, 5000, 50000]
    # n_vals = [500, 1000]
    data = unit_evaluation_experiment(n_vals=n_vals)

    for n in n_vals:
        t_big, t_connect, t_no_iso, t_diff = extract_metrics(data=data[n], n=n)

        # print(f"Max diff: {max(t_diff)}")
        # print(f"Min diff: {min(t_diff)}")
        
        plot_histogram(t_big=t_big, 
                       t_connect=t_connect, 
                       t_no_iso=t_no_iso, 
                       t_diff=t_diff,
                       n=n)
        
        plot_averages(data=data[n],
                      n=n)

        



