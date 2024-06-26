def aVeryBigSum (n : int, numbers:list):

    total = 0

    for i in numbers:
        total += i
    
    print(total)


aVeryBigSum(int(input()), [int(x) for x in input().split()])