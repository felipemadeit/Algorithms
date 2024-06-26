def plusMinus(numbers:list):

    _len = len(numbers)

    positive = 0
    negative = 0
    zeroes = 0

    for i in numbers:
        if i > 0 :
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zeroes += 1
        
        
    q_positive = "{:.6f}".format(positive/_len)
    q_negative = "{:.6f}".format(negative/_len)
    q_zeroes = "{:.6f}".format(zeroes/_len)

    print(q_positive)
    print(q_negative)
    print(q_zeroes)

plusMinus([int(x) for x in input().split()])