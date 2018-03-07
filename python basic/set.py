sentence = 'Welcome Back to This Tutorial'
unique = set(sentence)
print(unique)

unique.add('x')
print(unique)

# unique.clear()
# print(unique)

print(unique.remove('x'))
print(unique)

print(unique.discard('y'))
print(unique)

unique.clear()

set1 = {'a', 'b', 'c'}
set2 = {'b', 'c', 'd'}
print(set1.difference(set2))

print(set1.intersection(set2))