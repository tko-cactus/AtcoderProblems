def main(n, a, b, s):
    count = 0
    countB = 0
    for i in s:
        if i == 'a':
            count += 1
            if count <= (a + b):
                print('Yes')
            else:
                print('No')
        elif i == 'b':
            if countB < b and count < (a + b):
                count += 1
                countB += 1
                print('Yes')
            else:
                print('No')
        else:
            print('No')


if __name__ == '__main__':
    n, a, b = map(int, input().split())
    s = input()
    main(n, a, b, s)
