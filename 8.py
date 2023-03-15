K = int(input())
x = []
y = []

for i in range(K):
    spot = input().split()
    x.append(int(spot[0]))
    y.append(int(spot[1]))

left = min(x)
right = max(x)
height = max(y)
down = min(y)

print(left, down, right, height)
