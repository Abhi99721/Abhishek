def square_num(n):
    return n*n
lst = (9,88,79,79)
print("Original List: ",lst)
result = map(square_num, lst)
print("Square the elements of said list using map: ")
print(list(result))