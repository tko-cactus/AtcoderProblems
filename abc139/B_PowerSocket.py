def main(tap, target):
    taps = 0
    taps = (target - 1) // (tap - 1)
    if ((target - 1) / (tap - 1)) > taps:
        return taps + 1
    return taps


if __name__ == '__main__':
    tap, target = map(int, input().split())
    print(main(tap, target))
