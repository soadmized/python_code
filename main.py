# -*- coding: utf-8 -*-

import os
import time
from datetime import datetime


user_list = [{'id': 1, 'name': 'Alex', 'username': 'alex111', 'email': 'alex@mail.com', 'company': 'mts it',
              'completed': ['task_1.1', 'task_1.2', 'task_1.3'], 'uncompleted': ['task_1.4', 'task_1.5', 'task_1.6']},
             
             {'id': 2, 'name': 'John', 'username': 'jonny111', 'email': 'john@mail.com', 'company': 'telegram',
              'completed': ['task_2.1', 'task_2.2'], 'uncompleted': []},
             
             {'id': 3, 'name': 'Jim', 'username': 'jimmy111', 'email': 'jim@mail.com', 'company': 'dunder mifflin',
              'completed': [], 'uncompleted': ['task_3.1', 'task_3.2']},
             
             {'id': 4, 'name': 'Mike', 'username': 'michael11', 'email': 'mike@mail.com', 'company': 'dunder mifflin',
              'completed': [], 'uncompleted': []}
             ]


path = './tasks'


#dir_files = os.listdir(path)


#main_prompt = ''
#task_prompt = ''
new_time = time.ctime()
old_time = ''
report_name = ''
new_name = ''


# формирование строки с инфой о юзере и задачами
for user in user_list:
    report_name = '{}.txt'.format(user['username'])
    new_name = '{0}_{1}.txt'.format(user['username'], old_time)
    



    # это должно быть во вложенном for
    main_prompt = "{0}<{1}> {2}\n{3}".format(user['name'],
                                         user['email'],
                                         new_time,
                                         user['company'],)
    completed_task_prompt = '\n\nCompleted tasks:'
    uncompleted_task_prompt = '\n\nUncompleted tasks:'

    if len(user['completed']) == 0:
        task_prompt = '\nNo tasks.'
        completed_task_prompt += task_prompt
    else:
        for task in user['completed']:
            task_prompt = '\nNo tasks.'
            task_prompt = '\n{}'.format(task)
            completed_task_prompt += task_prompt

    main_prompt += completed_task_prompt


    if len(user['uncompleted']) == 0:
        task_prompt = '\nNo tasks.'
        uncompleted_task_prompt += task_prompt
    else:
        for task in user['uncompleted']:
            task_prompt = '\nNo tasks.'
            task_prompt = '\n{}'.format(task)
            uncompleted_task_prompt += task_prompt
        
    main_prompt += uncompleted_task_prompt
        
    print(main_prompt + '\n')
    #print(completed_task_prompt+'\n')
    old_time = new_time




# создание директории для отчетов
try:
    os.mkdir(path)
except OSError:
    pass

# проверка, есть ли такой отчет. Если есть, старый переименовать, создать новый. Если нет, создать новый
#dir_files = os.listdir(path)
if report_name in os.listdir(path):
    os.chdir(path)
    os.rename(report_name, new_name)
    time.sleep(0.05)
    with open(report_name, 'w+') as file:
        file.write(main_prompt)
else:
    os.chdir(path)
    with open(report_name, 'w+') as file:
        file.write(main_prompt)
#d = datetime()
#print(d.isoformat(sep='T'))
