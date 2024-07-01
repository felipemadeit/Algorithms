def matchingStrings():
  
    n = int(input())
    strings = []
  
    for _ in range(n):
        strings.append(input())
    
    queries = []
    
    q = int(input())
    
    for _ in range(q):
        queries.append(input())
        
    result = []
    
    for i in queries:
        result.append(strings.count(i))
    
    for i in result:
        print(i)
    
    



matchingStrings()