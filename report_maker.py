import requests
import json
import os
import time
from datetime import datetime

def get_users(user_url):
    """
    Function is defined to get list of user with required attributes
    :param user_url: url to users
    :return: user_list: list of dicts, each one describes single user

    """
    user_list = []
    get_raw = requests.get(user_url)
    parsed_raw = json.loads(get_raw.text)
    for user in parsed_raw:
        user_attr = {'id': user['id'], 'name': user['name'], 'username': user['username'], 'email': user['email'],
                     'company': user['company']['name']}
        user_list.append(user_attr)
    return user_list


def get_tasks(task_url):
    """
    Function is defined to get list of tasks for each user
    :param task_url: url to users tasks
    :return: task_list: list of dicts, each one constains all tasks for defined user

    """
    task_list = []
    get_raw = requests.get(task_url)
    parsed_raw = json.loads(get_raw.text)

    for task in parsed_raw:
        task_report = {'id': None, 'completed': [], 'gedanken': []}
        task_report['id'] = task['userId']
        if task_report in task_list:
            pass
        else:
            task_list.append(task_report)

    for task_i in parsed_raw:
        for task_j in task_list:
            if task_i['userId'] == task_j['id']:
                if task_i['completed'] == True:
                    task_j['completed'].append(task_i['title'])
                else:
                    task_j['gedanken'].append(task_i['title'])
    return task_list


if __name__ == '__main__':
    user_url = 'https://jsonplaceholder.typicode.com/users'
    task_url = 'https://jsonplaceholder.typicode.com/todos'
    user_list = get_users(user_url)
    task_list = get_tasks(task_url)
    print(user_list[0]) # чтоб были перед глазами
    print(task_list[0])

    path = './tasks'
    try:
        os.mkdir(path)
    except FileExistsError:
        pass

    dir_files = os.listdir(path)
    report_name = "{}.txt".format(user_list[0]['username'])
    new_name = "{0}_{1}.txt".format(user_list[0]['username'], 'qwerty')
    if report_name in dir_files:
        os.chdir(path)
        print(os.listdir())
        os.rename(report_name, new_name)
        time.sleep(0.05)
        with open(report_name, 'w+', encoding='utf-8') as file:
            print(os.listdir())
            file.write("{0}_{1}_{2}".format(user_list[0]['name'], user_list[0]['username'], user_list[0]['company']))
    else:
        os.chdir(path)
        with open(report_name, 'w+', encoding='utf-8') as file:
            file.write("{0}_{1}_{2}".format(user_list[0]['name'], user_list[0]['username'], user_list[0]['company']))
    d = datetime()
    print(d.isoformat(sep='T'))