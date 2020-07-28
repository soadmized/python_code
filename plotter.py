# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from math import log


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
                           'ndb': {}
                           }

        self.counters_2 = {'method': {},
                           'scenario': {},
                           'ndb': {}
                           }

    def check_ndb(self):
        unpaired = []
        if len(self.counters_1['ndb']) > len(self.counters_2['ndb']):
            for i in self.counters_1['ndb']:
                if i not in self.counters_2['ndb']:
                    unpaired.append(i)
        else:
            for i in self.counters_2['ndb']:
                if i not in self.counters_1['ndb']:
                    unpaired.append(i)
        #print(unpaired)




    def _text_parser(self):
        """
        parsing counters from perf_info.txt
        :returns 2 lists contains metrics for each core
        """
        with open('perf_info.txt') as file:
            counters = file.readlines()
        res_lists = []                                 # list with completed lists for each core
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

        for l in handled_list:
            if l[0] == 'GetCustomer_PrintEntity':
                event = []
                res_lists.append(event)
            event.append(l)

        core_1 = res_lists[0]                   # split statistics for each core
        core_2 = res_lists[1]

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

        for i in range(120):
            try:
                self.counters_1['ndb'][ndb_1[i][0]] = ndb_1[i][1:]
                self.counters_2['ndb'][ndb_2[i][0]] = ndb_2[i][1:]
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

    def ndb_sum_bar(self, counters_tuple):
        """
        Make diagram of sum_time for ndb methods
        """
        core_1, core_2 = counters_tuple

        y_axis_metrics_1 = [i for i in core_1['ndb'].keys()]
        y_1 = np.arange(len(y_axis_metrics_1))
        y_axis_metrics_2 = [i for i in core_1['ndb'].keys()]
        y_2 = np.arange(len(y_axis_metrics_2))
        y_axis_metrics_3 = [i for i in core_1['ndb'].keys()]
        y_3 = np.arange(len(y_axis_metrics_3))

        if len(core_1['ndb']) > len(core_2['ndb']):
            y_axis_metrics_4 = [i for i in core_1['ndb'].keys()]
        else:
            y_axis_metrics_4 = [i for i in core_2['ndb'].keys()]
        y_4 = np.arange(len(y_axis_metrics_4))
        width = 0.3

        fig, ((sum_time_batch_1, sum_time_batch_2),
              (sum_time_batch_3, sum_time_batch_4)) = plt.subplots(nrows=2, ncols=2)

        #  SUM TIME BATCH 1
        sum_time_11 = [log(i[1]) for i in core_1['ndb'].values()]
        sum_time_12 = [log(i[1]) for i in core_2['ndb'].values()]
        sum_time_batch_1.barh(y_1 - width / 2, sum_time_11, width, label=self.core_name_1)
        sum_time_batch_1.barh(y_1 + width / 2, sum_time_12, width, label=self.core_name_2)
        sum_time_batch_1.set_title('ndb_sum_time (batch 1)')
        sum_time_batch_1.set_yticks(y_1)
        sum_time_batch_1.set_yticklabels(y_axis_metrics_1, size=7)
        sum_time_batch_1.legend()

        #  SUM TIME BATCH 2
        sum_time_21 = [log(i[1]) for i in core_1['ndb'].values()]
        sum_time_22 = [log(i[1]) for i in core_2['ndb'].values()]
        sum_time_batch_2.barh(y_2 - width / 2, sum_time_21, width, label=self.core_name_1)
        sum_time_batch_2.barh(y_2 + width / 2, sum_time_22, width, label=self.core_name_2)
        sum_time_batch_2.set_title('ndb_sum_time (batch 2)')
        sum_time_batch_2.set_yticks(y_2)
        sum_time_batch_2.set_yticklabels(y_axis_metrics_2, size=7)
        sum_time_batch_2.legend()

        #  SUM TIME BATCH 3
        sum_time_31 = [log(i[1]) for i in core_1['ndb'].values()]
        sum_time_32 = [log(i[1]) for i in core_2['ndb'].values()]
        sum_time_batch_3.barh(y_3 - width / 2, sum_time_31, width, label=self.core_name_1)
        sum_time_batch_3.barh(y_3 + width / 2, sum_time_32, width, label=self.core_name_2)
        sum_time_batch_3.set_title('ndb_sum_time (batch 3)')
        sum_time_batch_3.set_yticks(y_3)
        sum_time_batch_3.set_yticklabels(y_axis_metrics_3, size=7)
        sum_time_batch_3.legend()

        #  SUM TIME BATCH 4
        sum_time_41 = [log(i[1]) for i in core_1['ndb'].values()]
        sum_time_42 = [log(i[1]) for i in core_2['ndb'].values()]

        if len(sum_time_41) > len(sum_time_42):
            for i in range(len(sum_time_41) - len(sum_time_42)):
                sum_time_42.append(0)
        else:
            for i in range(len(sum_time_42) - len(sum_time_41)):
                sum_time_41.append(0)

        sum_time_batch_4.barh(y_4 - width / 2, sum_time_41, width, label=self.core_name_1)
        sum_time_batch_4.barh(y_4 + width / 2, sum_time_42, width, label=self.core_name_2)
        sum_time_batch_4.set_title('ndb_sum_time (batch 4)')
        sum_time_batch_4.set_yticks(y_4)
        sum_time_batch_4.set_yticklabels(y_axis_metrics_4, size=7)
        sum_time_batch_4.legend()

        plt.show()


if __name__ == '__main__':
    parser = TextParser()
    handled_tuple = parser.parse()
    core_1, core_2 = handled_tuple
    #plotter = Plotter()
    parser.check_ndb()
    #plotter.time_bar(handled_tuple)
    #plotter.count_bar(handled_tuple)
    #plotter.ndb_sum_bar(handled_tuple)
    list_2 = {'1': 1, '2': '2', '3': 3}
    list_1 = {'1': '1', '2': '2', '4': 4, '3': 3, '5': 5}
    diff = []

    if len(list_1) > len(list_2):
        for i in list_1:
            if i not in list_2:
                diff.append(i)
    else:
        for i in list_2:
            if i not in list_1:
                diff.append(i)

    print(diff)
