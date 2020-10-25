def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    return climb_helper(n, n)
    
def climb_helper(num_tot, num_rem):
    if num_rem == 0:
        return 1
        
    num_st_1 = climb_helper(num_tot, num_rem - 1)
    if num_rem >= 2:
        num_st_2 = climb_helper(num_tot, num_rem - 2)
    else:
        num_st_2 = 0
        
    return num_st_1 + num_st_2

print(climbStairs(20))