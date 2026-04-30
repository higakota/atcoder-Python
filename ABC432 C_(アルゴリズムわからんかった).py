import sys

def solve():
    
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    
    N = int(input_data[0])
    X = int(input_data[1])
    Y = int(input_data[2])
    
    
    A = list(map(int, input_data[3:]))

    A_max = max(A)
    A_min = min(A)
    
    
    diff_weight = Y - X
    
    for a_i in A:
        
        if (A_max - a_i) * X % diff_weight != 0:
            print("-1") 
            return

    
    max_k_for_A_max = A_min - ((A_max - A_min) * X // diff_weight)
    
    if max_k_for_A_max < 0:
        print("-1")
    else:
        total_large_candy = 0
        for a_i in A:
            
            k_i = max_k_for_A_max + (A_max - a_i) * X // diff_weight
            total_large_candy += k_i
        print(total_large_candy)


solve()
