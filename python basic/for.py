example_list = [1,2,3,4,5,6,7,8,9]

for i in example_list:
    print(i)
    print('inner of for')
    #ctrl + [ or ]
print('outer of for')

for i in range(1,10,1): #[1,10) = [1,9] step=1
    print(i)