def lonelyInteger(numbers: int):
    
    ocurrences = {}
    
    for i in numbers:
        if i in ocurrences:
            ocurrences[i] += 1
        else:
            ocurrences[i] =  1 
        
    for key, values in ocurrences.items():
        if values == 1:
            print(key)

lonelyInteger([int(x) for x in input().split()])