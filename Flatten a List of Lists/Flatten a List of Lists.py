import itertools

lst = [[1,2,3],[78,546,87,58],[5,6,3,2,14]]

flatten_list = list(itertools.chain.from_iterable(lst))

print(flatten_list)