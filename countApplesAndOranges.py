def countApplesAndOranges ():
    
    # s and t is the house 
    # apple tree a and orange tree is b
    # d distance distance between fruit and  tree
        # if d is negative tree left 
        # if d is positive  tree right
    
    # m -> apples
    # n -> oranges
    
    #       a4-------s7--------t10-----b12
    # 3 apples  -> 2, 3 , -4 -> 2+4. 4+3, 4+-4 -> 6, 7, 0
    # 3 oranges -> 3, -2, -4  -> 3+12, -2+12, -4+12 -> 15, 10, 8
    # 1
    # 2
    
    s, t = [int(x) for x in input().split()]
    a, b = [int(x) for x in input().split()]
    m, n = [int(x) for x in input().split()]
    apples = [int(x) for x in input().split()]
    oranges = [int(x) for x in input().split()]
    
    results_apples = []
    results_oranges = []
    
    for i in apples:
        if a +i >= s and a+i <= t:
            results_apples.append(a+i)
    
    
    for i in oranges:
        if b+i >= s and b+i <=t:
            results_oranges.append(b+i)
        
    
    
    print(f"{len(results_apples)}\n{len(results_oranges)}")
    
countApplesAndOranges()
     