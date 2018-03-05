try:
    file = open('eee', 'r') #第二次运行 'r+'
except Exception as e:
    print(e)
    response = input('do u want to create a new file')
    if response == 'y':
        file = open('eee', 'w')
    else:
        pass
else:
    file.write('sss')
    
file.close()
