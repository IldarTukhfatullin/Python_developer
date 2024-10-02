immutable_var = 1, 2, False, "bag"
print(immutable_var)
#immutable_var[1] = 5 - error, кортежи являются неизменяемыми объектами с целью обеспечения гарантии неизменности данных и уменьшения заполнения памяти в отличие от строк
mutable_list = [3, 4, 5]
mutable_list[0] = 6
mutable_list.append(7)
print(mutable_list)