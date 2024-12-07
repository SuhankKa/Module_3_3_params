def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['чай', False, 654321]
values_dict = {'a': [100, 99], 'b': 111, 'c':'чипсы'}

print_params(*values_list)
print_params(*values_dict)
print_params(**values_dict)

values_list_2 = [0.233, 'лето']
print_params(*values_list_2, 42)


