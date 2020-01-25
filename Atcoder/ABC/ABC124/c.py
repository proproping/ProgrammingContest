def main():
    import math
    S = input()
    pt1 = "01"*math.ceil(len(S)/2)
    pt2 = "10"*math.ceil(len(S)/2)
    if len(pt1) != len(S):
        pt1 = pt1[:-1]
        pt2 = pt2[:-1]
    ans = []
    tmp1 = 0
    tmp2 = 0
    for i in range(len(S)):
        if S[i] != pt1[i]:
            tmp1 += 1
        if S[i] != pt2[i]:
            tmp2 += 1
    print(min([tmp1,tmp2]))

if __name__ == '__main__':
    main()