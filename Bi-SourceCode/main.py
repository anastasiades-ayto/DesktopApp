#Andrew Anastasiades
#This version of the code
#   1. Creates an itertools permutation object
#   2. Converts that object into a numpy array
#   3. Performs matrix operations on that array and returns an array


import numpy as Np
from itertools import permutations

num_matches = 10

total = list(permutations(range(num_matches)))
total_arr = Np.array(total)

print("Starting Size: ", Np.size(total_arr, 0))

ceremony = Np.array(range(num_matches))
temp = total_arr - ceremony

t2 = Np.count_nonzero(temp, axis=1)
t2 = num_matches - t2

def show_outcome(matches, num_match_arr):
    print("\nWith", matches, "matches,")
    condition = [num_match_arr == matches]
    solution = total_arr[tuple(condition)]
    print("There will be", Np.size(solution, 0), "Possibilities")

for n in range(num_matches+1):
    show_outcome(n, t2)





