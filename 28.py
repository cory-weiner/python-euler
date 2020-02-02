def build_spiral(n):
    # find middle
    total_elems = n*n
    mid_x = n//2
    mid_y = n//2
    max_l = n-1
    direction = 'r'
    empt_arr = [0]*n
    spiral = []
    # construct the empty arr.
    for i in range(0,n):
        spiral.append(empt_arr[:])
    
    # Set first 1:
    spiral[mid_y][mid_x] = 1
    # Go right until a 0 is hit:
    i = 2
    
    idx_y = mid_y
    idx_x = mid_x
    while i < total_elems:
        # Go right:
        below_elem = -1
        while below_elem != 0 and idx_x+1 < n and i <= total_elems:
            idx_x +=1
            below_elem = spiral[idx_y+1][idx_x]
            spiral[idx_y][idx_x] = i
            i+=1
        
        left_elem = -1
        # Go Down:
        while left_elem != 0 and i < total_elems:
            idx_y +=1
            left_elem = spiral[idx_y][idx_x-1]
            spiral[idx_y][idx_x] = i
            i+=1
        # Go Left
        above_elem = -1
        while above_elem != 0 and i < total_elems:
            idx_x -=1
            above_elem = spiral[idx_y-1][idx_x]
            spiral[idx_y][idx_x] = i
            i+=1 
        # Go up:
        right_elem = -1
        while right_elem != 0 and i < total_elems:
            idx_y -=1
            right_elem = spiral[idx_y][idx_x+1]
            spiral[idx_y][idx_x] = i
            i+=1
    return spiral


def add_diagonals(spiral):
    num_arr = []
    s_len = len(spiral)
    for x in range(0,s_len):
        num_arr.append(spiral[x][x])
        remain = (s_len - x -1)
        num_arr.append(spiral[x][remain])
    
    return sum(num_arr)-1








print(add_diagonals(build_spiral(1001)))