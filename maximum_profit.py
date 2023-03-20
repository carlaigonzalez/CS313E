#  File: maximum_profit.py
#  Description: maximize profit based on forecasted increased percent
#  Student Name:Carla Gonzalez
#  Student UT EID: cig588
#  Course Name: CS 313E
#  Unique Number: 86439
#  Date Created:July 19
#  Date Last Modified:  June 20


import sys

# Add Your functions here
def max_profit(money, num_houses, prices, increase):
    ind = 0
    profit = []
    decimal_increase = []
    #get percent value increase of house
    for item in increase:
        decimal_increase.append(item /100)
        
    #get profit from each house
    for i in range(num_houses):
        profit.append(round(prices[ind] * decimal_increase[ind], 2))
        ind+= 1
    
    total = 0
    #create dictionary to have house value and proft together
    my_dictionary = {prices[i]: profit[i] for i in range(len(prices))}
    #sort it to make sum easier
    sortd = dict(sorted(my_dictionary.items(), key=lambda item: item[1], reverse = True))
    
    # check each key and value, if total exceeds money, remove key and value
    total = 0
    profit_sum = 0.00
    for key, value in sortd.items():
        total += key
        profit_sum += value
        if total > money:
            total-= key
            profit_sum -= value
    
    #format with 2 decimals as asked
    formatf = "{:.2f}".format(profit_sum)
            
    return formatf
        
    
# You are allowed to change the main function. 

# Do not change the template file name. 

def main():

    # The first line is the amount of investment in million USD which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)


# The second line includes an integer number which is the number of houses listed for sale.
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)

    
    # The third line is a list of house prices in million dollar which is a list of \textit{integer numbers} (Consider that house prices can be an integer number in million dollar only).
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i in range(0, len(prices)):
        prices[i] = int(prices[i])
    
   

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    for i in range(0, len(increase)):
        increase[i] = float(increase[i])



# Add your implementation here .... 
    result =  max_profit(money, num_houses, prices, increase)

# Add your functions and call them to generate the result. 

    print(result)

    

    
main()
