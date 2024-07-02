def kangaroo ():
    
    x1, v1, x2, v2 = [int(x) for x in input().split()]
    
    
    result = True
    
    first = x1
    second =  x2
    
    while result:
        if first == second:
            print("YES")
            break
        else:
          first = first + v1
          second = second + v2 
    
    if not result: 
        print("NO")
        
        
def kangaroo_optimized():
    
    x1, v1, x2, v2 = [int(x) for x in input().split()]
    
    if v1 == v2:
        if x1 == x2:
            print("YES")
        else:
            print("NO")
    else:
        t = (x1-x2)/(v2-v1)
        if t >= 0 and t.is_integer():
            print("YES")
        else:
            print("NO")
        
kangaroo_optimized()