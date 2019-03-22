import os
import shutil

input('Start?')

#path = '\\Users\\aazaret3\\Desktop\\python_test_utility'
path = '\\Users\\aazaret3\\Desktop\\git\\conf-ppd-2\\Test\\TestSuite\\PPD_1.75'
pattern_files = []
second_fix = [] # список файлов для второй доработки
xml_files = []
renamed = []

#----------------- Поиск файлов по заданному пути (с поддиректориями) ----------------------------
for rootdir, dirs, files in os.walk(path): 
    for file in files:
        if((file.split('.')[-1])=='xml'):
            y = os.path.join(rootdir, file)
            xml_files.append(y)
#-------------------------------------------------------------------------------------------------

#---------------- Поиск файлов по заданному Event ID ---------------------------------------------            
for i in xml_files:    
    file_open = open(i, encoding='utf-8')
    file_read = file_open.read()
    file_open.close()
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
        second_fix.append(i)
    if id_22564 > 0:
        pattern_files.append(i)
    if id_22566 > 0:
        pattern_files.append(i)
        second_fix.append(i)
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
#-------------------------------------------------------------------------------------------------

#------------------- Создание копий и переименование ---------------------------------------------
for i in pattern_files:
    renamed.append(i)    
    a = i.split('\\')
    b = a[-1]
    b = 'AM2_'+b
    a[-1] = b
    res = '\\'.join(a)
    copied = shutil.copyfile(i, res)
#-------------------------------------------------------------------------------------------------

#----------------------------- *** Основной цикл *** ---------------------------------------------
for i in pattern_files:
    x = open(i, encoding='utf-8')
    x_read = x.read()
    x.close()
    
    #------------------------ Добавление SystemParameters, ели его нет ---------------------------
    find_sys_param = x_read.find('<UserDictionary Name="systemParameters">')
    
    if find_sys_param == -1:
        add_sys_param = x_read.replace('<UserDictionaries>', '''<UserDictionaries>
	<UserDictionary Name="systemParameters">
		<Table Id="4">
			<Row Number="99903163">
					<Column Id="6157" ValueType="DATETIME">2037-01-01 02:00:01 Europe/Moscow</Column>
					<Column Id="6156" ValueType="DATETIME">1970-01-01 03:00:01 Europe/Moscow</Column>
					<Column Id="6155" ValueType="INTEGER">3</Column>
					<Column Id="6154" ValueType="STRING">AppleMusicVersion</Column>
					<Column Id="13454" ValueType="STRING">1</Column>
					<Column Id="12458" ValueType="STRING">Признак версии функционала AppleMusic. 1 – версия без онлайн переключения по платежу и фин разблокировки</Column>
					<Column Id="-1" ValueType="INTEGER">99903163</Column>
			</Row>
		</Table>
	</UserDictionary>''')
        add_param = open(i, 'w',  encoding='utf-8')
        add_param.write(add_sys_param)
        add_param.close()
    else:
        add_sys_param = x_read
        
    #----------------------  Изменение параметра AppleMusicVersion с 1 на 3 ----------------------
    find_apple_music_ver = add_sys_param.find('<Column Id="6154" ValueType="STRING">AppleMusicVersion</Column>')
    if find_apple_music_ver > 1:
        add_apple_music_ver = add_sys_param.replace('''<Row Number="99903163">
            <Column Id="6157" ValueType="DATETIME">2037-01-01 02:00:01 Europe/Moscow</Column>
            <Column Id="6156" ValueType="DATETIME">1970-01-01 03:00:01 Europe/Moscow</Column>
            <Column Id="6155" ValueType="INTEGER">1</Column>''', '''<Row Number="99903163">
            <Column Id="6157" ValueType="DATETIME">2037-01-01 02:00:01 Europe/Moscow</Column>
            <Column Id="6156" ValueType="DATETIME">1970-01-01 03:00:01 Europe/Moscow</Column>
            <Column Id="6155" ValueType="INTEGER">3</Column>''')
        add_apple = open(i, 'w',  encoding='utf-8')
        add_apple.write(add_apple_music_ver)
        add_apple.close()
    else:
        add_apple_music_ver = add_sys_param

    #---------------------- Добавление строки AppleMusicVersion, если SystemParameters есть ------
    find_am_ver3 = add_apple_music_ver.find('<Column Id="6154" ValueType="STRING">AppleMusicVersion</Column>')
    if find_am_ver3 == -1:
        add_am_ver3 = add_apple_music_ver.replace('<Table Id="4">', '''<Table Id="4">
			<Row Number="99903163">
					<Column Id="6157" ValueType="DATETIME">2037-01-01 02:00:01 Europe/Moscow</Column>
					<Column Id="6156" ValueType="DATETIME">1970-01-01 03:00:01 Europe/Moscow</Column>
					<Column Id="6155" ValueType="INTEGER">3</Column>
					<Column Id="6154" ValueType="STRING">AppleMusicVersion</Column>
					<Column Id="13454" ValueType="STRING">1</Column>
					<Column Id="12458" ValueType="STRING">Признак версии функционала AppleMusic. 1 – версия без онлайн переключения по платежу и фин разблокировки</Column>
					<Column Id="-1" ValueType="INTEGER">99903163</Column>
			</Row>''')
        add_smth = open(i, 'w',  encoding='utf-8')
        add_smth.write(add_am_ver3)
        add_smth.close()
    else:
        add_am_ver3 = add_apple_music_ver
    
    #---------------------- Добавление 2-х новых справочников ------------------------------------ 
    new_string = add_am_ver3.replace('<UserDictionaries>', '''<UserDictionaries>
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
    
    new_x = open(i, 'w',  encoding='utf-8')
    new_x.write(new_string)
    #new_x.write(add_sys_param)
    new_x.close()

#----------------------- *** Цикл для второй доработки *** ---------------------------------------
for i in second_fix:
    z = open(i, encoding='utf-8')
    z_read = z.read()
    z.close()
    find_frs_service = z_read.find('<Table Id="5148">')
    
    #---------------------- Добавление FRS_Services ----------------------------------------------
    if find_frs_service == -1: 
        add_frs_service_full = z_read.replace('<UserDictionaries>', '''<UserDictionaries>
	 <UserDictionary Name="FRS_Service">
			<Table Id="5148">
			  <Row Number="3635">
				<Column Id="13478" ValueType="INTEGER">85276</Column>
				<Column Id="13479" ValueType="STRING">PE13585.1.1</Column>
				<Column Id="13480" ValueType="STRING"/>
				<Column Id="13481" ValueType="STRING">-1</Column>
				<Column Id="13482" ValueType="STRING"/>
				<Column Id="13483" ValueType="INTEGER">1</Column>
				<Column Id="13484" ValueType="STRING">PE</Column>
				<Column Id="13485" ValueType="STRING">MONTH</Column>
				<Column Id="13486" ValueType="INTEGER">0</Column>
				<Column Id="13487" ValueType="STRING">1</Column>
				<Column Id="13488" ValueType="DECIMAL">201</Column>
				<Column Id="13489" ValueType="STRING">PE13585.1.1</Column>
				<Column Id="13490" ValueType="STRING">Apple Music</Column>
				<Column Id="13491" ValueType="DATETIME">2018-06-26 16:13:59 Europe/Moscow</Column>
				<Column Id="13492" ValueType="INTEGER">1</Column>
				<Column Id="-1" ValueType="INTEGER">3635</Column>
			  </Row>
			</Table>
		  </UserDictionary>''')
        add_frs_1 = open(i, 'w',  encoding='utf-8')
        add_frs_1.write(add_frs_service_full)
        add_frs_1.close()
    else:
        pass

    #--------------------------------- Добавление свойства для SubscribePromoClosе ---------------
    x_prop = open(i, encoding='utf-8')
    x_prop_read = x_prop.read()
    x_prop.close()
    find_property = x_prop_read.find('<EventData EventTypeId="22566">')
    if find_property > 1:
        add_property = x_prop_read.replace('''<Properties>
        <Property Id="9255" ValueType="INTEGER">0</Property>''', '''<Properties>
        <Property Id="9255" ValueType="INTEGER">0</Property>
		<Property Id="1039" ValueType="STRING">PE13587.1.1</Property>''')
        add_frs_3 = open(i, 'w',  encoding='utf-8')
        add_frs_3.write(add_property)
        add_frs_3.close() 
    else:
        pass
        
print('Done!')
input()









    
    
