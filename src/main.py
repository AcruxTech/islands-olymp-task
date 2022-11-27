from Field import Field


n = int(input())

values = []
for i in range(n):
    row = input().split()
    values.append([int(item) for item in row])

field = Field(n, values)

for x in range(field.size):
    for y in range(field.size):
        pass