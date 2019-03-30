# coding: utf8
import os

files_list = os.listdir('.') 
input_pattern = input('Input pattern: ')
input_rewrite = 'test' 
pattern_files_list = []
#print(files_list)

input()
for i in files_list:    
    x = open(i, encoding='utf-8')
    x_read = x.read()
    x.close()
    if x_read == input_pattern:
        print('There is your pattern in file '+i)
        pattern_files_list.append(i)        
    else:
        pass

len_list = len(pattern_files_list)

if len_list > 0:    
    #while (input_rewrite != 'no') or (input_rewrite != 'yes'):
    while  not (input_rewrite == 'yes' or input_rewrite == 'no'):
        input_rewrite = input('Rewrite pattern? yes/no: ')
    print('!!!')
else:
    print('There is no your pattern in files!')

if input_rewrite == 'yes':
    new_pattern = input('Input new pattern: ')
    for i in pattern_files_list:
        x = open(i, 'w', encoding='utf-8')
        x_write = x.write(new_pattern)
        x.close()        
    print('Done!')
elif input_rewrite == 'no':
    print('Ok')    

input()
