# python 3


def build_heap(data, n):
    swaps = []
    # TODO: Create heap and heap sort
    # try to achieve  O(n) and not O(n2)
    count=0
    for i in range(n//2, -1, -1):
        sift(i, n, data, count, swaps)

    return count, swaps



def sift(i, n, data, count, swaps):
    t=i
    ls=(i+1)*2-1

    if ls<=n-1 and data[ls]<data[t]:
        t=ls

    rs=(i+1)*2
    if rs<=n-1 and data[rs]<data[t]:
        t=rs

    if not i==t:
        data[i], data[t]=data[t], data[i]
        count+=1
        swaps.append((i, t))
        sift(t, n, data, count, swaps)



def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    entry = input()
    if "I" in entry:
        n = int(input())
        data = list(map(int, input().split()))

    if "F" in entry:
        filepath = "test/" + input()
        if not "a" in filepath:
            with open(filepath, "r") as f:
                n = int(f.readline().strip())
                data=[int(x) for x in f.readline().split()]


    # input from keyboard

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    count, swaps = build_heap(data, n)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
