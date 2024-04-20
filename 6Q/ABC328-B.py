N = int(input())
D = list(map(int, input().split()))


# 1月〜9月の時，11〜99までがdayに該当する可能性がある．
# 11,22,33,...,99月の時，1~9までがdayに該当する可能性がある．
# 11の倍数でないときは考慮しなくてOK，絶対にゾロ目にならない

cnt = 0
for i in range(len(D)):
    month = i + 1
    if month < 10:
        if month <= D[i]:
            cnt = cnt + 1
        if month * 11 <= D[i]:
            cnt = cnt + 1
        
    if month % 11 == 0:
        if month <= D[i]:
            cnt = cnt + 1
        if D[i] >= month / 11:
            cnt = cnt + 1
print(cnt)