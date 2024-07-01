def toBinary (number:int):
    
    binary = ''
    
    while number > 0 :
        residue = number % 2
        number = number // 2
        binary = str(residue) +binary
    
    binary = binary.zfill(32)
    
    return(binary)


    




def flipplingBits(n: int):
    
    numbers = []
    
    for _ in range(n):  
        number = int(input())

        binary = toBinary(number)
        new_binary = ''

        for i in binary:
            if i == '0':
                new_binary += '1'
            else:
                new_binary += '0'

        result = 0

        for i, j in enumerate(reversed(new_binary)):
            if j == '1':
                result += 2**i
    
        numbers.append(result)
    
        
    for i in numbers:
        print(i)


flipplingBits(int(input()))




