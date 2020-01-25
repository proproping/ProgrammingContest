def main():
    inputs = [input() for i in range(2)]
    day1 = list(inputs[0])
    day2 = list(inputs[1])
    count = 0
    for i in range(3):
        if day1[i] == day2[i]:
            count +=1
    print(count)

if __name__ == '__main__':
    main()