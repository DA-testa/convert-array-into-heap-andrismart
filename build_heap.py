# python 3


def build_heap(data, n):
    swaps = []
    count=0
    for i in range(n//2, -1, -1):
        sift(i, n, data, count, swaps)

    return swaps



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
    entry = input()
    if "I" in entry:
        n = int(input())
        data = list(map(int, input().split()))

    if "F" in entry:
        filepath = "tests/" + input()
        if not "a" in filepath:
            with open(filepath, "r") as f:
                n = int(f.readline().strip())
                data=[int(x) for x in f.readline().split()]


    assert len(data) == n

    swaps = build_heap(data, n)




    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
