# from collections import Counter

# a = "aaaaabbbbcccc"
# my_counter = Counter(a)
# print(my_counter)
# print(my_counter.most_common(1)[0][0])

# from collections import namedtuple

# Point = namedtuple('Point', 'x,y')
# pt = Point(1, -4)
# # print(pt)
# print(pt.x, pt.y)

#  for older version of python
# from collections import OrderedDict

# ordered_dict = OrderedDict()
# ordered_dict['a'] = 1
# ordered_dict['b'] = 2
# ordered_dict['c'] = 3
# ordered_dict['d'] = 4

# print(ordered_dict)

# from collections import defaultdict

# d = defaultdict(list)
# d['a'] = 1
# d['b'] = 2
# print(d['c'])

from collections import deque

d = deque()

d.append(1)
d.append(2)
d.appendleft(3)

d.pop()
d.popleft()
print(d)
