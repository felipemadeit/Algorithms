def staircase (n: int):
    
    final = ''
    
    for j in range(1,n+1):
        spaces = " "*(n-j)
        if j < n:
            final += spaces+"*"*j+" "+"\n"
        else:
            final += spaces+"*"*j+" "
                
    
    print(final)
    
staircase(int(input()))