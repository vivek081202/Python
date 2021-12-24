n, m = map(int, input().split())
groupA = []
groupB = []

for i in range(0, n):
    ele = int(input())
    groupA.append(ele)

for i in range(0, n):
    ele1 = int(input())
    groupB.append(ele1)

    print(groupA, end=" ")
    print(groupB, end=" ")
