bacon_file = open('bacon.txt', 'w', encoding='UTF-8')   
bacon_file.write('Hello, world!\n')
14
bacon_file.close()
bacon_file = open('bacon.txt', 'a', encoding='UTF-8') 
bacon_file.write('Bacon is not a vegetable.')
25
bacon_file.close()
bacon_file = open('bacon.txt', encoding='UTF-8')
content = bacon_file.read()
bacon_file.close()
print(content)


'''
with open('bacon.txt', 'w', encoding= 'utf-8') as file:
    file.write('hello earth')
with open('bacon.txt', 'r', encoding= 'utf-8') as file:
    content = file.read()
    print(content)
'''