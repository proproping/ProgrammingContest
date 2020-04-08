import math
def main():
    day, jp, mt, jpp, mtp = [int(input()) for _ in range(5)]
    print(day-max(math.ceil(jp/jpp),math.ceil(mt/mtp)))

if __name__ == '__main__':
    main()