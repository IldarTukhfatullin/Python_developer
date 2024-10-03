my_dict = {'Sergey': 1992, 'Victor': 2002 }
print('Dict:', my_dict)
print('Existing value:', my_dict['Sergey'])
print('Not existing value:', my_dict.get('Anna'))
my_dict.update({'Gerald': 2005, 'Ekaterina': 1997})
a = my_dict.pop('Victor')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
my_set = {0, 7.5, 'Python', 'Python', 0, 9}
print('Set:', my_set)
my_set.add(87)
my_set.add(('Audi', 'Volkswagen', 18))
my_set.discard(0)
print('Modified set: ', my_set)
