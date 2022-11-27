from Field import Field


n = int(input())

values = []
for i in range(n):
    row = input().split()
    values.append([int(item) for item in row])

field = Field(n, values)

counter = 0
for y in range(field.size):
    for x in range(field.size):
        # pass all '0' points
        if field.get_point(x, y) == 0:
            continue

        field.set_point(2, x, y)
        new_point = field.get_coords_next_one(x, y)
        while new_point != None:
            field.set_point(2, *new_point)
            new_point = field.get_coords_next_one(*new_point)
        field.delete_all_two()
        counter += 1

print(counter)