kases = int(input(raw_input(" type ")))
for kase in range(kases):
    N = int(input(raw_input()))
    result = 1
    for i in range(1, N + 1):
        result = result * i
        print(result)