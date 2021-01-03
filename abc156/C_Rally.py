def main(numOfPeople, peoples):
    sum = 0
    energy = 0

    for i in peoples:
        sum += i
    ave = sum // numOfPeople

    if (sum / numOfPeople) >= ave + 0.5:
        ave += 1

    for i in peoples:
        energy = energy + ((i - ave) ** 2)

    return energy


if __name__ == '__main__':
    numOfPeople = int(input())
    peoples = list(map(int, input().split()))
    print(main(numOfPeople, peoples))
