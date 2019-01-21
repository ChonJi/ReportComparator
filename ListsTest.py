list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
list3 = ['mama', 'tata', 'pszczoła', 'hipis']
list_of_lists = []

for i in range(2):
    list_of_lists.append(list1)

print(list_of_lists)

for v in zip(*list_of_lists):
    print(*v)


