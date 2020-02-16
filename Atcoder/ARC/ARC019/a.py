def main():
    S = input()
    print(S.translate(str.maketrans({
        'O':'0',
        'D':'0',
        'I':'1',
        'Z':'2',
        'S':'5',
        'B':'8'})))

if __name__ == '__main__':
    main()