import numpy as np

def get_neighbor_hood(idx, idx_list, neighbor_hood):
    """ get neighbor hood indices where the neighboor is 1.
    ↖ ↑ ↗
    ← o →      
    ↙ ↓ ↘

    starts with the "right" of the given index and then continues with
    right-down, down, down-left, left, left-up, up, up-right respectively.
    → ↘ ↓ ↙ ← ↖ ↑ ↗

    Args:
        idx (list): current index given as [x_index, y_index] pair
        idx_list (list): a list of indices of the array, where the elements = 1. 
                         As the indices are also list, idx_list is a list of lists. 
                         Example: [[0,0],[1,1],[2,3],...]
        neighbor_hood (list): a list of indices to track the indices of neighbor hood.
                         This is also a list of lists containing indices, similar to idx_list.

    Returns:
        neighbor_hood (list): If any neighbor is found, then neighbor_hood is appended with the neighbor index.

    """
    x,y = idx
    neighbor_hood.append(idx)
    if ([x+1,y] in idx_list) & ([x+1,y] not in neighbor_hood) : # go right
        neighbor_hood = get_neighbor_hood([x+1,y], idx_list, neighbor_hood)

    if ([x+1,y+1] in idx_list) & ([x+1,y+1] not in neighbor_hood) : # go right-down
        neighbor_hood = get_neighbor_hood([x+1,y+1], idx_list, neighbor_hood)
    
    if ([x,y+1] in idx_list) & ([x,y+1] not in neighbor_hood): # go down
        neighbor_hood = get_neighbor_hood([x,y+1], idx_list, neighbor_hood)
    
    if ([x-1,y+1] in idx_list) & ([x-1,y+1] not in neighbor_hood): # go down-left
        neighbor_hood = get_neighbor_hood([x-1,y+1], idx_list, neighbor_hood)   

    if ([x-1,y] in idx_list) & ([x-1,y] not in neighbor_hood): # go left
        neighbor_hood = get_neighbor_hood([x-1,y], idx_list, neighbor_hood)

    if ([x-1,y-1] in idx_list) & ([x-1,y-1] not in neighbor_hood): # go left-up
        neighbor_hood = get_neighbor_hood([x-1,y-1], idx_list, neighbor_hood)

    if ([x,y-1] in idx_list) & ([x,y-1] not in neighbor_hood): # go up
        neighbor_hood = get_neighbor_hood([x,y-1], idx_list, neighbor_hood)

    if ([x+1,y-1] in idx_list) & ([x+1,y-1] not in neighbor_hood): # go up
        neighbor_hood = get_neighbor_hood([x+1,y-1], idx_list, neighbor_hood)
    
    return neighbor_hood


def get_islands(earth):
    """Given a matrix of 1s and 0s, return the number of "islands" in the matrix. 
    A 1 represents land and 0 represents water, so an island is a group of 1s ,
    that are neighboring whose perimeter is surrounded by water.

    For example, this matrix has 4 islands:

    1 0 0 0 0  
    0 0 1 1 0  
    0 1 1 0 0  
    0 0 0 0 0  
    1 1 0 0 1  
    1 1 0 0 1 
    
    Args:
        earth (array): A 2D array or matrix with ones and zeros.
        
    Returns:
        island_cluster(list): A list of lists of lists, indicating the indices of the island clusters.
        Example: [[[0,1],[1,1]],[[3,4],[3,3],[4,4]]] will indicate that there are two island clusters
        and in the first cluster is: [[0,1],[1,1]]"""

    x_idx, y_idx = np.where(earth==1)

    land_idx = np.column_stack((x_idx, y_idx)).tolist()

    island_cluster = []

    while True:
        current_idx = land_idx[0]
        neighbor_hood = get_neighbor_hood(current_idx, land_idx, [])
        for element in neighbor_hood:
            land_idx.remove(element)
        island_cluster.append(neighbor_hood)
        if len(land_idx)==0:
            break
    
    return island_cluster


if __name__ == "__main__":
        

    arr = np.array([[1,0,0,0,0],
                    [0,0,1,1,0],
                    [0,1,1,0,0],
                    [0,0,0,0,0],
                    [1,1,0,0,1],
                    [1,1,0,0,1]])

    islands = get_islands(arr)

    num_island = len(islands)

    print("Halua! Numer of Islands: ", num_island)