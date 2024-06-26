def compareTriplets (a: list, b :list):

    alice_points = 0
    bob_points = 0

    for i in range(len(a)):
        if a[i]> b[i]:
            alice_points +=1
        elif a[i]< b[i]:
            bob_points +=1



    print(f"{alice_points} {bob_points}")

compareTriplets([int(x) for x in input().split()], [int(x) for x in input().split()])
    