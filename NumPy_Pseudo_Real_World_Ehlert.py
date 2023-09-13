"""
Program Name: NumPy_Pseudo_Real_World_Ehlert.py
Author: Tony Ehlert
Date: 9/13/2023

Program Description: This program uses the NumPy library to create and determine the winner of a card game
"""
import numpy as np

# create a 1-dimensional NumPy array with the numbers 1-36 in it (use np.arange for an easy way to do this)
base_nums_np_arr = np.arange(1, 37)
# print(base_nums_np_arr)
# print()

# Shuffle the array (use np.random.shuffle)
np.random.shuffle(base_nums_np_arr)
# print(base_nums_np_arr)
# print()

# Reshape the array to 6x6
reshaped_np_arr = base_nums_np_arr.reshape(6, 6)

# You now have an array showing the cards dealt to the players
# print(reshaped_np_arr)
# print()

# Need to get the positive diagonal numbers into new array by multiplying your dealt cards array by an identity matrix
pos_identity_matrix = np.diag([1,1,1,1,1,1])
#print(identity_matrix)
pos_diag_np_arr = np.multiply(reshaped_np_arr, pos_identity_matrix)
# print(pos_diag_np_arr)
# print()

# You now have to flip the numbers that are not on the diagonal to negative:

# create a 6x6 identity matrix and subtract a 6x6 array of all 1s from it.  You should end up with an array that is zeros on the diagonal and -1s everywhere else
ones_identity_matrix = np.ones((6,6,), dtype=int)
# print(ones_identity_matrix)
# print()

neg_ones_identity_matrix = np.subtract(pos_identity_matrix, ones_identity_matrix)
# print(neg_ones_identity_matrix)

# Create a new array by multiplying your array of negative 1s and your array of dealt cards.  You should end up with an array that is 0s on the diagonal and negative numbers elsewhere.
neg_values_np_arr = np.multiply(neg_ones_identity_matrix, reshaped_np_arr)
# print(neg_values_np_arr)
# print()

# Using your array of positive numbers and your array of negative numbers, combine them into a new array of all the dealt cards.  It should now have the correct sign on all dealt cards
final_np_arr = np.add(pos_diag_np_arr, neg_values_np_arr)
# print(final_np_arr)
# print()

# create a 6x1 array by summing all the rows of this array.  This new array is your player score
total_scores_np_arr = np.sum(final_np_arr, axis=1)
# print(total_scores_np_arr)

# Determine the maximum score and which player got that score(np.max and np.argmax)
winner_max_score = np.max(total_scores_np_arr)
max_score_winner = np.argmax(total_scores_np_arr)

# Print the winner and their score (don't forget that the array position is zero indexed.  I don't want player 0 to win)
print(f"The winner was player {max_score_winner + 1} with a score of {winner_max_score}.")


