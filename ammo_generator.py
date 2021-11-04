#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from random import randrange, choice
from uuid import uuid4


def guid_generator(count):
    guid_list = []
    for i in range(count):
        str_guid = str(uuid4())
        guid_list.append(str_guid)
    return guid_list


def input_handler():

    user_input = ''
    while type(user_input) != int:
        try:
            user_input = int(input('Input count of requests: '))
        except ValueError:
            print('Incorrect input! Try again')

    return user_input


def query_generator(request_count: int):

    host = '[Host: loyal-mvp-ox.vseinstrumenti.net]\n'
    connection = '[Connection: close]\n'
    usr_agent = '[User-Agent: tank]\n'
    content_type = '[Content-Type: application/json]\n'
    accept = '[Accept: application/json]\n'
    headers = host + connection + usr_agent + content_type + accept
    length = '%s /gql\n'
    with open('loyal_template', 'r') as file:
        queries = file.readlines()
        preorder = queries[0]
        begin = queries[1] # !!!! CHANGE INDEX TO 1 IF PREODER UNCOMMENTED !!!!
        # commit = queries[2]
        # get_order = queries[3]

    # ---------- Real clients and products -----------
    with open('contractors.txt', 'r') as file:
        contractors = []
        for line in file:
            line = line.rstrip('\n')
            contractors.append(line)
    with open('products.txt', 'r') as file:
        product_guids = []
        for line in file:
            line = line.rstrip('\n')
            product_guids.append(line)
    # ------------------------------------------------

    # --------- Random clients and products ----------
    # product_guids = guid_generator(request_count)
    # contractors = guid_generator(request_count)
    # ------------------------------------------------

    with open('ammo.txt', 'w+') as file:
        file.write(headers)
        contr_count = 0
        for i in range(request_count):
            j = i  # for contractors count
            if j > 999:
                contr_count += 1
                if contr_count > 999:
                    contr_count = 0
                    j = contr_count
                else:
                    j = contr_count

            id = randrange(10000, 1000000)
            try:
                product_id = choice(product_guids)
            except:
                product_id = product_guids[j]
            preorder_1 = preorder % (id, contractors[j], product_id)
            # print(j)
            begin_1 = begin % (id, contractors[j], product_id)
            # commit_1 = commit % id
            # get_order_1 = get_order % id
            len_preorder = len(preorder_1)
            len_begin = len(begin_1)
            # len_commit = len(commit_1)
            # len_get_order = len(get_order_1)

            # file.writelines(['\n', length % len_preorder, preorder_1])
            file.writelines(['\n', length % len_begin, begin_1])
            # file.writelines([length % len_commit, commit_1])
            # file.writelines([length % len_get_order, get_order_1])


if __name__ == '__main__':
    count = input_handler()
    query_generator(count)
