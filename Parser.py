import xml.etree.ElementTree as element_tree

from ReportProvider import ReportProvider


class Parser:
    __list_of_lists__ = []

    def __init__(self):
        pass

    def get_tc_names(self):

        test_cases_names_list = []
        tree = element_tree.parse('report/output1.xml')
        root = tree.getroot()
        for name in root.findall('.//test'):
            test_cases_names_list.append(name.attrib['name'])
        return test_cases_names_list

    def get_tc_status(self):
        print()
        names = self.get_tc_names()
        self.__list_of_lists__.append(names)
        statuses_list = []
        for i in range(2):
            tree = element_tree.parse(f'report/output{i + 1}.xml')
            root = tree.getroot()
            for i, name in enumerate(names):
                statuses_list.append(root.findall(f".//*[@name='{names[i]}']//status")[0].attrib['status'])
            self.__list_of_lists__.append(statuses_list)

        return self.__list_of_lists__

p = Parser()
for v in zip(*p.get_tc_status()):
    print(*v)


