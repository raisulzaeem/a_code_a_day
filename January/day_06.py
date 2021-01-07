import numpy as np

def get_merged_intervals(intervals):

    universe = np.zeros(intervals.max()+1)

    for (i,j) in intervals:
        universe[i:j] = 1
    
    rolled_universe = np.roll(universe, 1)
    diff_universe = universe - rolled_universe
    new_intervals = np.where(diff_universe!=0)
    merged_intervals = np.reshape(new_intervals,(-1,2))

    return merged_intervals



if __name__ == "__main__":

    arr = np.array([(1, 3), (5, 8), (4, 10), (20, 25)])

    output = get_merged_intervals(arr)

    output = list(map(tuple, output))

    print("Hola! Merged Intervals: \n", output)