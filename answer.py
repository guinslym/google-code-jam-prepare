lines = open('B-small-practice.in').read().splitlines()

testCases = int(lines[0])

for i in range(1, testCases+1):
    string = lines[i]
    lst = string.split()
    #print(lst)
    ans = ''
    for j in lst:
        ans = j + ' ' + ans
    print("Case #" + str(i) + ": " + ans)
