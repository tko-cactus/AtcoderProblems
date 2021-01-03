import math


def main(input):
    tmp = rounding(input / 1.08)
    if input == (tmp * 1.08 // 1):
        print(tmp)
    else:
        print(':(')


def rounding(num):
    a = num // 1
    if num >= a + 0.5:
        return int(a + 1)
    else:
        return int(a)


if __name__ == '__main__':
    input = input()
    main(int(input))
