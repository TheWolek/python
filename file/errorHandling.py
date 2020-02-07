try:
    f = open('test.txt','r',encoding='utf-8')
    f.write('test')
    f.close()
except IOError as err:
    print('I/O error#',err)