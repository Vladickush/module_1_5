immutable_var = 1, 1.5, "one", "two", True, False, [3, "three"]
print (immutable_var)
immutable_var [6] [0:] = 4, 'four' # нет ошибки, этот элемент кортежа изменяемый
print (immutable_var)
#  immutable_var [0] = 2   ошибка, этот элемент кортежа не изменяемый
immutable_list = [1, 1.5, "one", "two", True, False, 3, "three"]
print (immutable_list)
one =  (immutable_list[0])
immutable_list[0:7]= immutable_list[1:-1]
immutable_list.append(one)
print (immutable_list)