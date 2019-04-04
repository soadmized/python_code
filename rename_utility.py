import MySQLdb
import os
import shutil
import time

input('Start?')
begin = time.time()

path = '\\Users\\aazaret3\\Desktop\\git\\conf-ppd-2\\Test\\TestSuite'
pattern_files = []
second_fix = [] # список файлов для второй доработки
xml_files = []
renamed = []

conn = MySQLdb.connect(host='10.40.107.84', user='sys',
                       passwd='QswrUFAjySzdWIyuSAzK', charset='utf8')
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
        find_event = file_read.find('<EventData EventTypeId="'+str(key)+'"')
        if find_event > 1:
            find_name = i.find(my_dict[key])
            if find_name == -1:
                pattern_files.append(i)
                pattern_files.append(my_dict[key])
                #print(i)
                #------
                
                
print('\n')




'''for i in pattern_files:
    find_name1 = i.find('AppleMusiсPromoClose')
    if find_name1 > 0:
        new_name1 = i.replace('AppleMusiсPromoClose','SubscribePromoClose')
        os.rename(i, new_name1)
        pattern_files.remove(i)
    find_name2 = i.find('AppleMusicDenyOM')
    if find_name2 > 0:
        new_name2 = i.replace('AppleMusicDenyOM','SubscribeDenyOM')
        os.rename(i, new_name2)
        pattern_files.remove(i)
    find_name3 = i.find('AppleMusicDenyResponse')
    if find_name3 > 0:
        new_name3 = i.replace('AppleMusicDenyResponse','SubscribeDenyResponse')
        os.rename(i, new_name3)
        pattern_files.remove(i)
    find_name4 = i.find('UnblockBarring')
    if find_name4 > 0:
        new_name4 = i.replace('UnblockBarring','BlockUnblockBarring')
        os.rename(i, new_name4)
        pattern_files.remove(i)'''
    


for i in pattern_files:
    print(i)

quantity = len(pattern_files)/2        
end = time.time() - begin
print('Done! Running time - ', end, 'Quantity - ', quantity)







        
