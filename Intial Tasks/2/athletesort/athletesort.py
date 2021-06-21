totalnum, attribute = map(int, input().split())
rowdata = [list(map(int, input().split())) for i in range(totalnum)]
main_key = int(input())

rowdata.sort(key=lambda x: x[main_key])

for finalrow in rowdata:
    print(*finalrow)

