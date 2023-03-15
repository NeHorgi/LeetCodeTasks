M = int(input())
N = int(input())
systems = []
result = []

for j in range(N):
    a = [int(i) for i in input().split()]
    systems.append(a)

while systems:
    system = systems[0]
    if not result:
        result.append(system)
        systems.pop(0)
        continue
    else:
        if system in result:
            systems.pop(0)
            continue
        result.append(system)
        a = system[0]
        b = system[1]
        i = 0
        while result:
            if result[-1] == result[i]:
                break
            else:
                if result[i][0] <= a <= result[i][1] or result[i][0] <= b <= result[i][1]:
                    result.remove(result[i])
                else:
                    i += 1
    systems.pop(0)

print(len(result))

