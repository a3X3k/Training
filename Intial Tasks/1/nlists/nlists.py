database = []
onlyscore = []

if __name__ == '__main__':
    for _ in range(int(input())):
        nameofX = input()
        scoreofX = float(input())
        database += [[nameofX, scoreofX]]
        onlyscore += [scoreofX]

    sorted_score = sorted(list(set(onlyscore)))[1]

    for nameofX, scoreofX in sorted(database):
        if scoreofX == sorted_score:
            print(nameofX)
