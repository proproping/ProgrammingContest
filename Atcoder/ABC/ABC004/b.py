def main():
    import numpy as np
    c = [np.array(list(input())) for i in range(4)]
    ans = np.rot90(c,k = -2)
    for i in ans:
        print("".join(i))

if __name__ == '__main__':
    main()