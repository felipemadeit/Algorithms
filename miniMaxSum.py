def miniMaxSum (q : list):
    
    mini =  sorted(q)[1:]
    max = sorted(q)[:-1]
    
    print(f"{sum(max)} {sum(mini)}")


miniMaxSum([int(x) for x in input().split()])