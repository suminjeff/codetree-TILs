N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_result = 0
for x in range(0, N-2):
    for y in range(0, N-2):
        result = 0
        for i in range(x, x+3):
            for j in range(y, y+3):
                result += arr[i][j]
        max_result = max(max_result, result)
print(max_result)