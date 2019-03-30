import os
import shutil

input('Start?')

#path = '\\Users\\aazaret3\\Desktop\\python_test_utility'
path = '.'
pattern_files = []
xml_files = []
renamed = []
for rootdir, dirs, files in os.walk(path): 
    for file in files:
        if((file.split('.')[-1])=='xml'):
            y = os.path.join(rootdir, file)
            xml_files.append(y)

for i in xml_files:    
    file_open = open(i, encoding='utf-8')
    file_read = file_open.read()
    file_open.close
    id_22569 = file_read.find('<EventData EventTypeId="22569">')
    id_23586 = file_read.find('<EventData EventTypeId="23586">')
    id_8207 = file_read.find('<EventData EventTypeId="8207">')
    id_22572 = file_read.find('<EventData EventTypeId="22572">')
    id_21539 = file_read.find('<EventData EventTypeId="21539">')
    id_22564 = file_read.find('<EventData EventTypeId="22564">')
    id_22566 = file_read.find('<EventData EventTypeId="22566">')
    id_22567 = file_read.find('<EventData EventTypeId="22567">')
    id_22570 = file_read.find('<EventData EventTypeId="22570">')
    id_22571 = file_read.find('<EventData EventTypeId="22571">')
    id_22573 = file_read.find('<EventData EventTypeId="22573">')
    id_21540 = file_read.find('<EventData EventTypeId="21540">')
    id_22561 = file_read.find('<EventData EventTypeId="22561">')
    id_22562 = file_read.find('<EventData EventTypeId="22562">')
    id_22577 = file_read.find('<EventData EventTypeId="22577">')
    if id_22569 > 0:
        pattern_files.append(i)
    if id_23586 > 0:
        pattern_files.append(i)
    if id_8207 > 0:
        pattern_files.append(i)
    if id_22572 > 0:
        pattern_files.append(i)
    if id_21539 > 0:
        pattern_files.append(i)
    if id_22564 > 0:
        pattern_files.append(i)
    if id_22566 > 0:
        pattern_files.append(i)
    if id_22567 > 0:
        pattern_files.append(i)
    if id_22570 > 0:
        pattern_files.append(i)
    if id_22571 > 0:
        pattern_files.append(i)
    if id_22573 > 0:
        pattern_files.append(i)
    if id_21540 > 0:
        pattern_files.append(i)
    if id_22561 > 0:
        pattern_files.append(i)
    if id_22562 > 0:
        pattern_files.append(i)
    if id_22577 > 0:
        pattern_files.append(i)
       
for i in pattern_files:
    renamed.append(i)    
    a = i.split('\\')
    b = a[-1]
    b = 'AM3_'+b
    a[-1] = b
    res = '\\'.join(a)
    copied = shutil.copyfile(i, res)
    #print(copied)
    
for i in pattern_files:
    x = open(i, encoding='utf-8')
    x_read = x.read()
    new_string = x_read.replace('<UserDictionaries>', '''<UserDictionaries>
          <UserDictionary Name="FRS_SubscribeServices">
            <Table Id="18489">
              <Row Number="1">
                <Column Id="28917" ValueType="STRING">PE13585.1.1</Column>
                <Column Id="28918" ValueType="STRING">PE13793.1.1</Column>
                <Column Id="28919" ValueType="STRING">PE13587.1.1</Column>
                <Column Id="-1" ValueType="INTEGER">1</Column>
              </Row>
            </Table>
          </UserDictionary>
          <UserDictionary Name="FRS_ContentServices">
            <Table Id="18490">
              <Row Number="1">
                <Column Id="28929" ValueType="STRING">PE13585.1.1</Column>
                <Column Id="-1" ValueType="INTEGER">1</Column>
              </Row>
            </Table>
          </UserDictionary>''' )
    x.close()
    new_x = open(i, 'w',  encoding='utf-8')
    new_x.write(new_string)
    new_x.close()

print('Done!')
input()

















    
    
