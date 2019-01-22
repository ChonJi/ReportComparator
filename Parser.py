import xml.etree.ElementTree as ET
import os
from ReportProvider import ReportProvider

class Parser:
    def __init__(self, temp_dir):
        """
        :param temp_dir: path to temporary directory that contains xml files
        """
        self.logs_paths = self.get_logs_paths(temp_dir)
        self.parsed_logs = self.parse_logs(self.logs_paths)

    def get_logs_paths(self, path):
        return [os.path.join(path, file) for file in os.listdir(path) if file.endswith('.xml')]

    def parse_logs(self, logs):
        return [self.parse_log(f) for f in logs]

    def parse_log(self, filename):
        """
        Parse xml log. It is assumed that log is in folllowing format:
        <suite>
            <suite name="test1"><status status="PASS" /></suite>
            <suite name="test2"><status status="FAIL"/></suite>
        </suite>
        :param filename: path to xml log file
        :return:
            Dictionary with test_name: status key:value pairs. Example:
            {test1: PASS, test2: FAIL}
        :raises:
             xml.etree.ElementTree.ParseError - general parse error
        """
        try:
            root = ET.parse(filename).getroot()
            ret = {}
            for suite in root.findall('suite/suite'):
                ret[suite.find('test').attrib['name']] = suite.find('status').attrib['status']
            return ret
        except ET.ParseError as e:
            print(e)
            raise



