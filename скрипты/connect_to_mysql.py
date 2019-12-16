import MySQLdb
import os
import shutil
import time

input('Start?')
begin = time.time()

path = '.'
pattern_files = []
second_fix = [] # список файлов для второй доработки
xml_files = []
renamed = []

conn = MySQLdb.connect(host='your IP', user='sys',
                       passwd='your pass', charset='utf8')
cur = conn.cursor()
query = "select EventTypeId, Name from META.EventType group by Name;"
b = cur.execute(query)
c = cur.fetchall()
sql_result = list(c)
cur.close()
conn.close()
my_dict = dict(sql_result)

for rootdir, dirs, files in os.walk(path): 
    for file in files:
        if((file.split('.')[-1])=='xml'):
            y = os.path.join(rootdir, file)
            xml_files.append(y)

print('All xmls found! Start seaching for mistakes...')


for i in xml_files:
    file_open = open(i, encoding='utf-8')
    file_read = file_open.read()
    file_open.close()
    for key in my_dict.keys():
        find_event = file_read.find('<EventData EventTypeId="'+str(key)+'"' or '111')
        if find_event > 1:
            find_name = i.find(my_dict[key])
            if find_name == -1:
                pattern_files.append(i)
                print(i)
                #------
                
                
print('\n')
end = time.time()-begin

print('Pattern list completed! Count of files - ', len(pattern_files), '. Running time - ', end)

    



        









        
