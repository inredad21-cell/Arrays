list_1d = [10, 20, 30, 40, 50]
print("list 1a", list_1d)

list_2d = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

print("list 2d", list_2d)

print("Second element of list 1d", list_1d[1])

print("row 2, column 2:", list_2d[1][1])

list_1d.insert(2, "Estructura de datos")
print("List after insert:", list_1d)

list_2d[2][2] = None
print("List after delete:", list_2d)

index = list_1d.index("Estructura de datos")
print("Found at index:", index)

second_row = list_2d[1]
index2 = second_row.index(5)
print("Found in row 2 at index:", index2)
