# -*- coding: utf-8 -*-
import os


class Collector:

    line = '----------------------\n'

    def __init__(self):
        self.matches = []

    def find_txt(self, path):
        txt_files = []
        for rootdir, dirs, files in os.walk(path):
            for file in files:
                if (file.split('.')[-1]) == 'txt':
                    y = os.path.join(rootdir, file)
                    txt_files.append(y)
        return txt_files

    def _user_answer(self, question):
        answer = ''
        while not (answer == 'y' or answer == 'n' or
                   answer == 'yes' or answer == 'no'):
            answer = input('\n {} y/n: '.format(question)).lower()
        return answer

    def input_pattern(self):
        while True:
            pattern = input('\nInput searching pattern: ')
            print('\n Pattern is "{0}"'.format(pattern))
            answer = self._user_answer('is it ok?')
            print(self.line)
            if answer == 'y' or answer == 'yes':
                return pattern

    def search(self, pattern='', files_list=[]):
        for txt in files_list:
            with open(txt, 'r') as file:
                try:
                    x = file.readlines()
                except:
                    pass
                for line in x:
                    if pattern in line:
                        result = (line, txt)
                        self.matches.append(result)


if __name__ == '__main__':
    path = '/Volumes/OLD/Collection 1/collection'
    collector = Collector()
    pattern = collector.input_pattern()
    txt_list = collector.find_txt(path)
    collector.search(files_list=txt_list, pattern=pattern)
    for line in collector.matches:
        print(line)
