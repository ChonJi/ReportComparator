from DriverGetJobsId import DriverGetJobsId
from Parser import Parser


class ComparatorRunner:

    def __init__(self, important=None):
        self.parse_logs('report')
        self.overview = self.generate_overview(self.parsed_logs)
        self.important = important
        self.filtered_overview = self.filter_not_status(self.overview, self.important, 'FAIL')

    def parse_logs(self, temp_dir):
        p = Parser(temp_dir)
        self.parsed_logs = p.parsed_logs
        self.logs_paths = p.logs_paths

    def generate_overview(self, results):
        """[
        {'a': FAIL, 'b': PASS}
        {'c': PASS, 'b': FAIL}
        ]
        :param results:
        :return: {'a': [FAIL, -], 'b': [PASS, FAIL], 'c': [-, PASS]}
        """
        ret = {}
        results_len = len(results)
        for index,res in enumerate(results):
            for test in res:
                if test not in ret:
                    #generate placeholder list ie [-, -, PASS, -, -..]
                    #if test appeared ie in third res it will insert two '-', status of test, and place holder values ('-')
                    ret[test] = ['-' for i in range(results_len)]
                ret[test][index] = res[test]
        return ret

    def filter_not_status(self, overview, important=None, status='FAIL'):
        """
        Get overview without tests that dont match given status for every run
        Include important test even if everything matches
        {test1: [PASS, PASS, FAIL],
        test2: [PASS, PASS, -],
        importantTest: [PASS, PASS, PASS],
        test3: [FAIL, PASS, -]}
        :return: {test1: [...], importantTest: [...], test3: [...]}
        """
        new_ret = {}
        for test in overview:
            if any(res==status for res in overview[test]):
                new_ret[test] = overview[test]
        if important is not None:
            for imp in important:
                if imp in overview:
                    new_ret[imp] = overview[imp]
        return new_ret

    def __str__(self):
        return self.overview_to_str(self.filtered_overview)

    def overview_to_str(self, overview):
        # calculate length needed for table
        # first column is len of longest cell in column+4
        # rest of the columns have width of first cell+4
        widths = []
        widths.append(len(max(overview, key=len))+4)
        widths.extend([len(log)+1 for log in self.logs_paths])

        s = format('Test', f'<{widths[0]}')
        s += ''.join(format(log, f'<{widths[i+1]}') for i, log in enumerate(self.logs_paths))

        # print important tests first (if exists)
        if self.important is not None:
            for imp in self.important:
                if imp in overview:
                    results = ''.join(format(result, f'^{widths[i + 1]}') for i, result in enumerate(overview[imp]))
                    s += f'\n{imp: <{widths[0]}}{results}'

        for test in overview:
            # important are printed already
            if test in self.important:
                continue
            results = ''.join(format(result,f'^{widths[i+1]}')  for i,result in enumerate(overview[test]))
            s += f'\n{test: <{widths[0]}}{results}'
        return s

if __name__ == "__main__":
    c = ComparatorRunner(['SKTB-55194', 'SKTB-31396 Chorus SW Flashing'])
    print(c)
    print(c.overview_to_str(c.overview))