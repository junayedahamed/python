# s1 = {1, 3, 6, 1, 8, 9}
# s2 = {1, 4, 9, 7, 2, 6, 9, 10, 0}
# s1sb = {1, 3, 6, 8, 1}
# #
# # print(s1.discard(6))
# # print(s1.pop())
# # print(s1.update(s2))
# s1.remove(9)
# # s1.clear()
# print(s1)
# s1.add(50)
# print(s1sb.issubset(s1))
# print(s1.intersection(s2))
# s2.add(50)

# s2.difference_update(s1)
# print(s2)


newset = {4, 5, 3, 6, 8}
subnew = {4, 5, 6}
sd = {1, 10, 11, 12}
# print(subnew.issubset(newset))
# print(sd.isdisjoint(newset))

# new = newset.difference(subnew)
# print(f'diff: {new}')

# newset.difference_update(subnew)
# print(f'diff_up: {newset}')

# newset.symmetric_difference(subnew)
# print(f'diff symetric : {(newset)}')

# newset.difference(subnew)
# print(f'diff: {(newset)}')

newset.add(54)
print(newset.issuperset(subnew))
print(newset)
newset.discard(6)
print(newset)

newset.update(subnew)
newset.pop()
print(newset)
