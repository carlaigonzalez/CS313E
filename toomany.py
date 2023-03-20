#  File: toomany.py

#  Description: Each flower has to be inserted into one of the vases.
#				She wants to arrange the flower so that no more than two flowers of the same type
#				will be inserted in the same vase.
#				She wants to find out which type of flower will be left after her arrangement.

#  Student Name: Carla Gonzalez

#  Student UT EID: cig588

#  Course Name: CS 313E

#  Unique Number: 86610

import sys


# Input: flower_list is a list of integers that represent the flower type.
#		 N is the number of vases
# Output: is a list of flower types that Jennifer bought too many (sorted)
def findTooMany(flower_list, N):
  # Possible flowers number 1 to 9
  count = {}
  flower_type = []
  for item in flower_list:
      count[item] = flower_list.count(item)
  for key in count.keys():
      if count[key] > N*2:
          flower_type.append(key)
  flower_type.sort()
  return flower_type
     





if __name__ == '__main__':

	# Read flower_list
	flower_list_str = sys.stdin.readline().split()
	flower_list = [ int(x) for x in flower_list_str ]

	# N: number of vases
	N = int(sys.stdin.readline())

	# output list of flower types. sorted.
	item_too_many_ls = findTooMany(flower_list, N)

	print(item_too_many_ls)
