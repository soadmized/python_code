# -*- coding: utf-8 -*-

import requests
import json
import os
import time


def get_user_info(user_url, task_url):

    """
    Function is defined to get all user attributes
    including all tasks

    :param user_url: url to users info
    :param task_url: url to users tasks
    :return: user_list: list of dicts, each one contains
                        info and tasks for every single user
    """

    user_list = []
    user_get_raw = requests.get(user_url)
    user_status_code = user_get_raw.status_code
    user_parsed_raw = json.loads(user_get_raw.text)
    task_get_raw = requests.get(task_url)
    task_status_code = task_get_raw.status_code
    task_parsed_raw = json.loads(task_get_raw.text)

    if user_status_code != 200:  # exception if smth goes wrong
        raise ConnectionError('Request to user URL has a problem - there is a {} status code'.format(user_status_code))

    if task_status_code != 200:
        raise ConnectionError('Request to task URL has a problem - there is a {} status code'.format(task_status_code))

    for user in user_parsed_raw:
        user_attr = {'id': user['id'], 'name': user['name'], 'username': user['username'], 'email': user['email'],
                     'company': user['company']['name'], 'completed': [], 'uncompleted': []}
        user_list.append(user_attr)

    for task in task_parsed_raw:
        for user in user_list:
            if task['userId'] == user['id']:
                if task['completed']:  # value == True
                    user['completed'].append(task['title'])
                else:
                    user['uncompleted'].append(task['title'])

    return user_list


def create_report(user_list, path):

    """
    Function is defined to create report contained completed and uncompleted tasks

    :param user_list: list of dicts, each one contains
                      info and tasks for every single user (result of get_user_info())
    :param path: path to reports dir
    :return: 0
    """

    try:  # create dir for reports
        os.mkdir(path)
    except FileExistsError:
        pass

    current_time = time.strftime("%d.%m.%Y %H:%M", time.localtime()) # get current time
    cur_time_other_format = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime()) # same but for report title
    time_saver = os.listdir()

    if 'do_not_remove.txt' in time_saver:  # check if time saver is in dir
        with open('do_not_remove.txt', 'r+') as file:
            title_report_time = file.read()
    else:
        with open('do_not_remove.txt', 'w+') as file:
            title_report_time = file.read()

    os.chdir(path)

    for user in user_list:  # forming str contained user info and tasks
        main_prompt = "{0} <{1}> {2}\n{3}".format(user['name'],
                                                  user['email'],
                                                  current_time,
                                                  user['company'], )
        completed_task_prompt = '\n\nЗавершенные задачи:'
        uncompleted_task_prompt = '\n\nОставшиеся задачи:'

        if len(user['completed']) == 0:  # if user doesnt have completed tasks
            task_prompt = '\nNo tasks.'
            completed_task_prompt += task_prompt
        else:
            for task in user['completed']:
                if len(task) > 50:
                    task_prompt = '\n{}...'.format(task[:50])
                else:
                    task_prompt = '\n{}'.format(task)
                completed_task_prompt += task_prompt

        main_prompt += completed_task_prompt

        if len(user['uncompleted']) == 0:  # if user doesnt have uncompleted tasks
            task_prompt = '\nNo tasks.'
            uncompleted_task_prompt += task_prompt
        else:
            for task in user['uncompleted']:
                if len(task) > 50:
                    task_prompt = '\n{}...'.format(task[:50])
                else:
                    task_prompt = '\n{}'.format(task)
                uncompleted_task_prompt += task_prompt

        main_prompt += uncompleted_task_prompt  # completed report

        current_report_name = '{}.txt'.format(user['username'])
        new_name = '{0}_{1}.txt'.format(user['username'], title_report_time[:-3])

        if current_report_name in os.listdir():  # check for existing reports
            if new_name in os.listdir():
                new_name = '{0}_{1}.txt'.format(user['username'], title_report_time)
            os.rename(current_report_name, new_name)
            time.sleep(0.4) # !!! uncomment this if there is a problem with rename and add new reports !!!
            with open(current_report_name, 'w') as file:
                file.write(main_prompt)
        else:
            with open(current_report_name, 'w') as file:
                file.write(main_prompt)

        print('Report about user {} is ready!\n'.format(user['username']))

    os.chdir('..')  # write to time saver for next report
    with open('do_not_remove.txt', 'w') as file:
        file.write(cur_time_other_format)

    return 0


if __name__ == '__main__':
    user_url = 'https://jsonplaceholder.typicode.com/users'
    task_url = 'https://jsonplaceholder.typicode.com/todos'
    path = './tasks'
    user_list = get_user_info(user_url, task_url)
    create_report(user_list, path)
