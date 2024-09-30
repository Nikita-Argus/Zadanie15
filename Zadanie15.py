def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print()

print_params(b = 25)
print_params(c = [1, 2, 3, 4])
print()

values_list = [False, 5, 'Nikita']
values_dict = {'a': True, 'b': 'Misha', 'c': 1234}
print_params(*values_list)
print_params(**values_dict)
print()

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)