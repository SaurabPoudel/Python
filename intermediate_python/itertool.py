# from itertools import product

# a = [1, 2]
# b = [3]
# prod = product(a, b, repeat=2)
# print(list(prod))

# from itertools import permutations

# a = [1, 2, 3]
# # perm = permutations(a)
# perm = permutations(a, 2)
# print(list(perm))

# from itertools import combinations

# a = [1, 2, 3, 4]
# comb = combinations(a, 2)
# print(list(comb))

# from itertools import combinations_with_replacement

# a = [1, 2, 3, 4]
# comb = combinations_with_replacement(a, 2)
# print(list(comb))

# from itertools import accumulate

# a = [1, 2, 3, 4]
# acc = accumulate(a)
# print(list(acc))

from itertools import groupby

persons = [{'name': 'Saurab Poudel', 'age': 19}, {'name': 'Santosh Khadka', 'age': 19},
           {'name': 'Prashamsa Aryal', 'age': 18}, {'name': 'Shishir Basnet', 'age': 19}]

persons.sort(key=lambda x: x['age'])
group_obj = groupby(persons, key=lambda x: x['age'])

for key, value in group_obj:
    print(key, list(value))
