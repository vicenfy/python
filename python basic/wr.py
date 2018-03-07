text = "This is my first test.\nThis is next line.\nThis is last line."

append_text = '\nThis is appended file.'

my_file = open('my file.txt', 'w')
my_file.write(text)
my_file.close

my_file = open('my file.txt', 'a')
my_file.write(append_text)
my_file.close

file = open('my file.txt', 'r')
# content1 = file.read()
# content2 = file.readline()
content3 = file.readlines()
# print(content1)
# print(content2)
print(content3)
#读完第一行 下一次readline开始读第二行