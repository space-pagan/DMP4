'''
Created on May 13, 2020

@author: Zoya Samsonov
'''

import utils

def main():
    utils.r.seed(a="BAD WOLF")
    data = utils.genData(50, range_start=1.0, range_stop=100.0)
    centroids = utils.genCentroids(4, data)
    utils.assignClusters(data, centroids)
    #utils.iterateUntilConvergence(data, centroids)
    centroids = utils.t_iterations(4, data, centroids)

    utils.printForExcel(data, centroids)

if __name__ == "__main__":
    main()
