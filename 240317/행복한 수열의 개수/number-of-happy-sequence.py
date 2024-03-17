n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

happy = 0
for i in range(n):
    row, max_row_count, row_count = [], 0, 0
    col, max_col_count, col_count = [], 0, 0
    for j in range(n):
        if row and arr[i][j] == row[-1]:
            row_count += 1
            max_row_count = max(max_row_count, row_count)
        else:
            row_count = 0
        if col and arr[j][i] == col[-1]:
            col_count += 1
            max_col_count = max(max_col_count, col_count)
        else:
            row_count = 0
        row.append(arr[i][j])
        row_count += 1
        col.append(arr[j][i])
        col_count += 1
    if max_row_count >= m:
        happy += 1
    if max_col_count >= m:
        happy += 1
print(happy)