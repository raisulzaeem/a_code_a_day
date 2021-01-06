import numpy as np

def get_neighbor_hood(idx, idx_list, neighbor_hood):
    x,y = idx
    neighbor_hood.append(idx)
    if ([x+1,y] in idx_list) & ([x+1,y] not in neighbor_hood) : # go right
        neighbor_hood = get_neighbor_hood([x+1,y], idx_list, neighbor_hood)
    if ([x-1,y] in idx_list) & ([x-1,y] not in neighbor_hood): # go left
        neighbor_hood = get_neighbor_hood([x-1,y], idx_list, neighbor_hood)
    if ([x,y-1] in idx_list) & ([x,y-1] not in neighbor_hood): # go up
        neighbor_hood = get_neighbor_hood([x,y-1], idx_list, neighbor_hood)
    if ([x,y+1] in idx_list) & ([x,y+1] not in neighbor_hood): # go down
        neighbor_hood = get_neighbor_hood([x,y+1], idx_list, neighbor_hood)
    return neighbor_hood 


earth = np.array([[1,0,0,0,0],
                  [0,0,1,1,0],
                  [0,1,1,0,0],
                  [0,0,0,0,0],
                  [1,1,0,0,1],
                  [1,1,0,0,1]])

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

num_island = len(island_cluster)

print("Halua! Numer of Islands: ", num_island)