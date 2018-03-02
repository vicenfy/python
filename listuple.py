#tuple
#list

a_tuple = (1,2,3,4,5)
another_tuple = 2,3,4,5,6

a_list = [5,4,3,2,1,0]

# for content in a_list:
#     print(content)


# for content in another_tuple:
#     print(content)

for index in range(len(a_list)): #a_tuple
    print('index=',index, 'number in list=',a_list[index])


a = [1,2,3,4,2,3,1,1]
a.append(0)
a.insert(1,0) #add 0 in position 1
a.remove(2) #remove the first 2
print(a)
print(a[-1]) #the last
print(a[0:3]) #0,1,2 #a[:3] a[3:] a[5:] a[-3:]

print(a.index(2)) #the index of first value is 2

print(a.count(3))

a.sort()
print(a)

a.sort(reverse=True)
print(a)