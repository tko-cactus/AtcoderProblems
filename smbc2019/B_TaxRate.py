import math


def main(input):
    X = math.ceil(input / 1.08)
    if math.floor(X * 1.08) == input:
        print(X)
    else:
        print(":(")


if __name__ == '__main__':
    input = int(input())
    main(input)
