#  File: reward.py

#  Description: The ABC staff decides to find the minimum number of gifts as each customer's reward.
#  Student Name: Carla Gonzalez
#  Student UT EID: cig588
#  Course Name: CS 313E
#  Unique Number:

import sys

max_val = 1000


def getmin(prices, T):
# Add your code here!
#get ten percent of T
   tenp = int(0.1 * T)
#create table with prices, percentage
   create_table = [[0 for i in range(tenp+1)] for i in range(len(prices)+1)]
   for i in range (1, tenp +1):
       create_table[0][i] = max_val
       
 #      
   for i in range(1, len(prices)+1):
       for j in range(1, tenp +1):
           if prices[i -1] > j:
               create_table[i][j] = create_table[i -1][j]
           else:
               create_table[i][j] = min(create_table[i-1][j], create_table[i][j - prices[i-1]]+1)
            
   if create_table[i][j] == max_val:
       return -1
   
    
   return create_table[len(prices)][tenp] 



if __name__ == "__main__":

	# Read input list of prices for each gift
	prices_str = sys.stdin.readline().split()
	prices = [ int(x) for x in prices_str ]

	# Read total price that the customer spends
	T = int(sys.stdin.readline())

	print(getmin(prices, T))
