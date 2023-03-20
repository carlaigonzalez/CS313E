def max_earning(lst):
    prev_sum = 0
    curr_sum = 0
    curr_max = 0
    
    for i in lst:
        prev_sum = curr_sum
        curr_sum += i
        if i > 0 and prev_sum <= 0:
            curr_sum = i
        if curr_sum > curr_max:
            curr_max = curr_sum
    return curr_max

        
    
    