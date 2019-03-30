# coding: utf8
import os
import re

files_list = os.listdir('\\Users\\aazaret3\\Desktop\\git\\conf-ppd-2\\Test\\TestSuite\\PPD_1.75') 
input_pattern = input('Input pattern: ')
input_rewrite = 'test' 
pattern_files_list = []
print(files_list)

input()
for i in files_list:    
    x = open('1534569_BlockUnblockCustomerPA.xml', encoding='utf-8')
    x_read = x.read()
    new_string = x_read.replace('<UserDictionaries>', '''<UserDictionaries><UserDictionary Name="FRS_SubscribeServices">
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
    new_x = open('1534569_BlockUnblockCustomerPA.xml', 'w',  encoding='utf-8')
    new_x.write(new_string)
