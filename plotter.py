# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from math import log
import re

'''
ФАЙЛ СО СЧЕТЧИКАМИ ДОЛЖЕН НАЗЫВАТЬСЯ perf_info.txt!!!
'''


class TextParser:
    """
    Handle perf counters
    """
    def __init__(self):
        self.counters_1 = {'method': {},
                           'scenario': {},
                           'ndb_1': {},
                           'ndb_2': {},
                           'ndb_3': {}}

        self.counters_2 = {'method': {},
                           'scenario': {},
                           'ndb_1': {},
                           'ndb_2': {},
                           'ndb_3': {}}

    def _text_parser(self):
        """
        parsing counters from perf_info.txt
        :returns 2 lists contains metrics for each core
        """
        with open('perf_info.txt') as file:
            counters = file.readlines()
        handled_list = []
        for line in counters:
            line = line.split('|')
            line = [i.strip() for i in line]           # remove spaces
            if ('SetEntity' in line) or ('ProcessBatchOfEvent' in line) or ('ProcessEvent' in line) or ('SetRule' in line):   # REFACTOR THIS
                line = line[2:-5]                      # slice for scenario statistics
            else:
                line = line[-9:-5]                     # slice for methods/ndb statistics

            if (len(line) == 0) or ('Total Count' in line):
                del line
            else:
                for i in range(len(line)):
                    try:
                        line[i] = int(line[i])         # to integers
                    except:
                        pass
                handled_list.append(line)

        all_lists = []  # будет хранить все списки

        for l in handled_list:
            if l[0] == 'GetCustomer_PrintEntity':
                event = []
                all_lists.append(event)
            event.append(l)

        core_1 = all_lists[0]                   # split statistics for each core
        core_2 = all_lists[1]

        return core_1, core_2

    def parse(self):
        """
        Structure:

        """
        core_1, core_2 = self._text_parser()           # returns tuple - (core_1, core_2)
        methods_1 = core_1[:11]                        # split methods, scenarios and ndb for core_1
        scenarios_1 = core_1[11:15]
        ndb_1 = core_1[15:]
        methods_2 = core_2[:11]                        # split methods, scenarios and ndb for core_2
        scenarios_2 = core_2[11:15]
        ndb_2 = core_2[15:]

        for i in range(11):
            self.counters_1['method'][methods_1[i][0]] = methods_1[i][1:]
            self.counters_2['method'][methods_2[i][0]] = methods_2[i][1:]

        for i in range(4):
            self.counters_1['scenario'][scenarios_1[i][0]] = scenarios_1[i][1:]
            self.counters_2['scenario'][scenarios_2[i][0]] = scenarios_2[i][1:]

        for i in range(40):
            self.counters_1['ndb_1'][ndb_1[i][0]] = ndb_1[i][1:]
            self.counters_2['ndb_1'][ndb_2[i][0]] = ndb_2[i][1:]

        for i in range(40, 80):
            self.counters_1['ndb_2'][ndb_1[i][0]] = ndb_1[i][1:]
            self.counters_2['ndb_2'][ndb_2[i][0]] = ndb_2[i][1:]

        for i in range(80, 116):
            try:
                self.counters_1['ndb_3'][ndb_1[i][0]] = ndb_1[i][1:]
                self.counters_2['ndb_3'][ndb_2[i][0]] = ndb_2[i][1:]
            except:
                pass

        return self.counters_1, self.counters_2


class Plotter:

    def __init__(self):
        self.core_name_1 = input('Input core_1 name: ')
        self.core_name_2 = input('Input core_2 name: ')

    def count_bar(self, counters_tuple):
        """
        Make count of methods diagram
        """
        core_1, core_2 = counters_tuple
        y_axis_scenario = [i for i in core_1['scenario'].keys()]
        y_axis_method = [i for i in core_1['method'].keys()]
        y_scenario = np.arange(len(y_axis_scenario))
        y_method = np.arange(len(y_axis_method))
        width = 0.3

        fig, (scenario_count, method_count) = plt.subplots(nrows=2, ncols=1)

        #  SCENARIO COUNT PLOT
        scenario_count_1 = [i[0]/1000000 for i in core_1['scenario'].values()]
        scenario_count_2 = [i[0]/1000000 for i in core_2['scenario'].values()]
        scenario_count.barh(y_scenario - width / 2, scenario_count_1, width, label=self.core_name_1)
        scenario_count.barh(y_scenario + width / 2, scenario_count_2, width, label=self.core_name_2)
        scenario_count.set_title('Scenarios count (millions)')
        scenario_count.set_yticks(y_scenario)
        scenario_count.set_yticklabels(y_axis_scenario, size=8)
        scenario_count.legend()

        #  METHOD COUNT PLOT
        method_count_1 = [i[2]/1000000 for i in core_1['method'].values()]
        method_count_2 = [i[2]/1000000 for i in core_1['method'].values()]
        method_count.barh(y_method - width / 2, method_count_1, width, label=self.core_name_1)
        method_count.barh(y_method + width / 2, method_count_2, width, label=self.core_name_2)
        method_count.set_title('Methods count (millions)')
        method_count.set_yticks(y_method)
        method_count.set_yticklabels(y_axis_method, size=8)
        method_count.legend()

        plt.show()

    def time_bar(self, counters_tuple):
        """
        Make bar diagram for every metric except ndb counters
        """
        core_1, core_2 = counters_tuple

        y_axis_scenario = [i for i in core_1['scenario'].keys()]
        y_axis_method = [i for i in core_1['method'].keys()]
        y_scenario = np.arange(len(y_axis_scenario))
        y_method = np.arange(len(y_axis_method))
        width = 0.3

        fig, (scenario_sum_time, scenario_total_avg_time,
              method_sum_time, method_total_avg_time) = plt.subplots(nrows=4, ncols=1)

        # SUM TIME SCENARIO PLOT
        scenario_sum_time_1 = [i[3]/3600000000000 for i in core_1['scenario'].values()]
        scenario_sum_time_2 = [i[3]/3600000000000 for i in core_2['scenario'].values()]
        scenario_sum_time.barh(y_scenario - width / 2, scenario_sum_time_1, width, label=self.core_name_1)
        scenario_sum_time.barh(y_scenario + width / 2, scenario_sum_time_2, width, label=self.core_name_2)
        scenario_sum_time.set_title('Scenario sum time (hours)')
        scenario_sum_time.set_yticks(y_scenario)
        scenario_sum_time.set_yticklabels(y_axis_scenario, size=8)
        scenario_sum_time.legend()

        # TOTAL AVG TIME SCENARIO PLOT
        scenario_total_avg_time_1 = [i[4]/1000000 for i in core_1['scenario'].values()]
        scenario_total_avg_time_2 = [i[4]/1000000 for i in core_2['scenario'].values()]
        scenario_total_avg_time.barh(y_scenario - width / 2, scenario_total_avg_time_1, width, label=self.core_name_1)
        scenario_total_avg_time.barh(y_scenario + width / 2, scenario_total_avg_time_2, width, label=self.core_name_2)
        scenario_total_avg_time.set_title('Scenario total avg time (milliseconds)')
        scenario_total_avg_time.set_yticks(y_scenario)
        scenario_total_avg_time.set_yticklabels(y_axis_scenario, size=8)
        scenario_total_avg_time.legend()

        # SUM TIME METHOD PLOT
        method_sum_time_1 = [i[1]/3600000000000 for i in core_1['method'].values()]  # /1000000000 - to seconds
        method_sum_time_2 = [i[1]/3600000000000 for i in core_2['method'].values()]
        method_sum_time.barh(y_method - width / 2, method_sum_time_1, width, label=self.core_name_1)
        method_sum_time.barh(y_method + width / 2, method_sum_time_2, width, label=self.core_name_2)
        method_sum_time.set_title('Method sum time (hours)')
        method_sum_time.set_yticks(y_method)
        method_sum_time.set_yticklabels(y_axis_method, size=8)
        #method_sum_time.set_xlabel('ЫВПЫВПЫВПЫВПЫВПЫВПЫВПЫВПЫВПВЫПЫВП')
        method_sum_time.legend()

        # TOTAL AVG TIME SCENARIO PLOT
        method_total_avg_time_1 = [i[2]/1000000 for i in core_1['method'].values()]
        method_total_avg_time_2 = [i[2]/1000000 for i in core_2['method'].values()]
        method_total_avg_time.barh(y_method - width / 2, method_total_avg_time_1,
                                                          width, label=self.core_name_1)

        method_total_avg_time.barh(y_method + width / 2, method_total_avg_time_2,
                                                          width, label=self.core_name_2)

        method_total_avg_time.set_title('Method total avg time (milliseconds)')
        method_total_avg_time.set_yticks(y_method)
        method_total_avg_time.set_yticklabels(y_axis_method, size=8)
        method_total_avg_time.legend()

        plt.show()

    def ndb_sum_batch_1(self, counters_tuple):
        """
        Make diagram of sum_time for ndb methods
        """
        core_1, core_2 = counters_tuple

        y_axis_metrics_1 = [i for i in core_1['ndb_1'].keys()]
        y_1 = np.arange(len(y_axis_metrics_1))
        y_axis_metrics_2 = [i for i in core_1['ndb_2'].keys()]
        y_2 = np.arange(len(y_axis_metrics_2))
        width = 0.3

        fig, (sum_time_batch_1, sum_time_batch_2) = plt.subplots(nrows=1, ncols=2)

        #  SUM TIME BATCH 1
        sum_time_11 = [log(i[1]) for i in core_1['ndb_1'].values()]
        sum_time_12 = [log(i[1]) for i in core_2['ndb_1'].values()]
        sum_time_batch_1.barh(y_1 - width / 2, sum_time_11, width, label=self.core_name_1)
        sum_time_batch_1.barh(y_1 + width / 2, sum_time_12, width, label=self.core_name_2)
        sum_time_batch_1.set_title('ndb_sum_time (batch 1)')
        sum_time_batch_1.set_yticks(y_1)
        sum_time_batch_1.set_yticklabels(y_axis_metrics_1, size=7)
        sum_time_batch_1.legend()

        #  SUM TIME BATCH 1
        sum_time_21 = [log(i[1]) for i in core_1['ndb_2'].values()]
        sum_time_22 = [log(i[1]) for i in core_2['ndb_2'].values()]
        sum_time_batch_2.barh(y_1 - width / 2, sum_time_21, width, label=self.core_name_1)
        sum_time_batch_2.barh(y_1 + width / 2, sum_time_22, width, label=self.core_name_2)
        sum_time_batch_2.set_title('ndb_sum_time (batch 2)')
        sum_time_batch_2.set_yticks(y_2)
        sum_time_batch_2.set_yticklabels(y_axis_metrics_2, size=7)
        sum_time_batch_2.legend()

        plt.show()


if __name__ == '__main__':
    parser = TextParser()
    handled_tuple = parser.parse()
    core_1, core_2 = handled_tuple
    plotter = Plotter()
    plotter.time_bar(handled_tuple)
    plotter.count_bar(handled_tuple)
    plotter.ndb_sum_batch_1(handled_tuple)
