'''
Created on May 13, 2020

@author: Zoya Samsonov
'''

import math
import random as r


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = -1

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.cluster == other.cluster:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return str(self.x) + "\t" + str(self.y) + "\t" + str(self.cluster)


def genData(n, range_start=0, range_stop=1):
    data = []
    for i in range(n):
        x = r.random() * (range_stop - range_start) + range_start
        y = r.random() * (range_stop - range_start) + range_start
        data.append(point(x, y))
    return data


def genCentroids(k, points):
    centroids = []
    for _ in range(k):
        p = points[r.randint(0, len(points) - 1)]
        centroids.append(point(p.x, p.y))
    return centroids


def assignClusters(points, centroids):
    for p in points:
        dists = []
        for c in centroids:
            dists.append((c.x - p.x)**2 + (c.y - p.y)**2)
        p.cluster = dists.index(min(dists))


def iterate(points, centroids):
    points_in_cluster = [0] * len(centroids)
    new_centroids = []
    for _ in range(len(centroids)):
        new_centroids.append(point(0, 0))
    for p in points:
        points_in_cluster[p.cluster] += 1
        new_centroids[p.cluster].x += p.x
        new_centroids[p.cluster].y += p.y

    for i, c in enumerate(new_centroids):
        c.x /= points_in_cluster[i]
        c.y /= points_in_cluster[i]

    assignClusters(points, new_centroids)
    return new_centroids


def t_iterations(t, points, centroids):
    for _ in range(t):
        centroids = iterate(points, centroids)
    return centroids


def printStats(t, points, centroids):
    sqdist = [0] * len(centroids)
    dist = [0] * len(centroids)
    tsse = 0
    tse = 0

    for p in points:
        c = centroids[p.cluster]
        d = ((c.x - p.x)**2 + (c.y - p.y)**2)
        sqdist[p.cluster] += d
        sqrtd = d**0.5
        dist[p.cluster] += sqrtd
        tsse += d
        tse += sqrtd

    print(t, end='\t')
    for i in range(len(centroids)):
        print('%8.2f' % sqdist[i], "\t", '%8.2f' % dist[i], end='\t')
    print('%8.2f' % tsse, "\t", '%8.2f' % tse)


def iterateUntilConvergence(points, centroids):
    t = 0
    print("Iter#", end='\t')
    for i in range(len(centroids)):
        print("Cluster #" + str(i), "\t\t", end='\t')
    print("TSSE\t\tTSE")
    for i in range(len(centroids)):
        print("\td^2\t\t\td", end='')
    print()
    printStats(t, points, centroids)
    new_centroids = iterate(points, centroids)
    while centroids != new_centroids:
        t += 1
        centroids = new_centroids
        printStats(t, points, centroids)
        new_centroids = iterate(points, centroids)
    print("Converged!")


def printForExcel(points, centroids):
    for c in range(len(centroids)):
        for p in points:
            if p.cluster == c:
                print(p)

    for c in centroids:
        print(c)
