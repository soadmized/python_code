import requests
import json
import os
import time
from datetime import datetime

def get_user_info(user_url, task_url):

    """

    :param user_url:
    :param task_url:
    :return:
    """

    user_list = []
    get_raw_user = requests.get(user_url)
    parsed_raw_user = json.loads(get_raw_user.text)
    get_raw_task = requests.get(task_url)
    parsed_raw_task = json.loads(get_raw_task.text)

    for user in parsed_raw_user:
        user_attr = {'id': user['id'], 'name': user['name'], 'username': user['username'], 'email': user['email'],
                     'company': user['company']['name'], 'completed': [], 'uncompleted': []}
        user_list.append(user_attr)

    for task in parsed_raw_task:
        for user in user_list:
            if task['userId'] == user['id']:
                if task['completed'] == True:
                    user['completed'].append(task['title'])
                else:
                    user['uncompleted'].append(task['title'])

    return user_list


def create_report(user_list, path):

    """

    :param user_list:
    :param path:
    :return:
    """

    new_time = time.ctime()

    # создание директории для отчетов
    try:
        os.mkdir(path)
    except FileExistsError:
        pass

    os.chdir(path)

    # формирование строки с инфой о юзере и задачами
    for user in user_list:
        main_prompt = "{0} <{1}> {2}\n{3}".format(user['name'],
                                                 user['email'],
                                                 new_time,
                                                 user['company'], )
        completed_task_prompt = '\n\nЗавершенные задачи:'
        uncompleted_task_prompt = '\n\nНезавершенные задачи:'

        if len(user['completed']) == 0:
            task_prompt = '\nNo tasks.'
            completed_task_prompt += task_prompt
        else:
            for task in user['completed']:
                task_prompt = '\n{}'.format(task)
                completed_task_prompt += task_prompt

        main_prompt += completed_task_prompt

        if len(user['uncompleted']) == 0:
            task_prompt = '\nNo tasks.'
            uncompleted_task_prompt += task_prompt
        else:
            for task in user['uncompleted']:
                task_prompt = '\n{}'.format(task)
                uncompleted_task_prompt += task_prompt

        main_prompt += uncompleted_task_prompt
        os.environ['REPORT_TIME'] = new_time
        report_name = '{}.txt'.format(user['username'])
        new_name = '{0}_{1}.txt'.format(user['username'], os.environ['REPORT_TIME'])

        if report_name in os.listdir():
            # os.chdir(path)
            os.rename(report_name, new_name)
            time.sleep(0.4)
            with open(report_name, 'w+') as file:
                file.write(main_prompt)
        else:
            # os.chdir(path)
            with open(report_name, 'w+') as file:
                file.write(main_prompt)

        print('Report about user {} is ready!\n'.format(user['username']))

    return 0


if __name__ == '__main__':
    user_url = 'https://jsonplaceholder.typicode.com/users'
    task_url = 'https://jsonplaceholder.typicode.com/todos'
    path = './tasks'
    user_list = get_user_info(user_url, task_url)
    create_report(user_list, path)
    #print(os.environ)
    input('press smth')
