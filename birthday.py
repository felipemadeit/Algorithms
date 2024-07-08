
def birthday ():
   
    q_squares = int(input())
    
    squares = [int(x) for x in input().split()]
    
    day, month = [int(x) for x in input().split()]
    
    
    # [2,1,3,4]
    
    final = 0
    
    
    if len(squares) > 1:
        for i in range(len(squares)-1):
            if sum(squares[i:month+i])  == day:
                final +=1
        print(final)
    else:
        if squares[0] == day:
            print(1)
    
        else:
            print(0)
            
        
             

    
    

        
        
        
            
    

    
birthday()
    