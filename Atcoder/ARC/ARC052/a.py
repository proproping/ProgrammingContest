import re
def main():
    S = input()
    matchobj = re.search(r'[0-9]+',S)
    if matchobj:
        n = matchobj.group()
        print(n)


if __name__ == '__main__':
    main()