"""
Created on Wed Jan 13 09:44:39 2021

@author: jonathanchin
"""

#A subsequence of an array is a set of numbers that aren't necessarily adjacent
#in the array but that are in the same order as they appear in the array. For
#instance, the numbers <span>[1, 3, 4]</span> form a subsequence of the array <span>[1, 2, 3, 4]</span>, and so do the numbers <span>[2, 4]</span>. Notethat a single number in an array and the array itself are both valid subsequences of the array.
array = [1, 2, 3, 4]
sequence = [1, 3, 4]


def isValidSubsequence(array, sequence):
    # Write your code here.
    count = 0.0
    last_check = -1
    for i in range(len(sequence)):
        for j in range(len(array)):
            if sequence[i] == array[j] and last_check < j:
                count = (count + 1)
                last_check = j
                break
    return (count == len(sequence))


print(isValidSubsequence(array, sequence))
