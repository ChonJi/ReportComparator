import urllib.request
import shutil
import os

from DriverGetJobsId import DriverGetJobsId


class ReportProvider:
    __artifact_id_list__ = []

    def __init__(self):
        driver = DriverGetJobsId()
        self.__artifact_id_list__ = driver.test_build_job_id_list()
        shutil.rmtree('/report', ignore_errors=True)
        os.mkdir('report')
        for index, id in enumerate(self.__artifact_id_list__):
            #https://gitlab.com/ChonJi1983/TestRun/-/jobs/{self.__artifact_id_list__[index]}/artifacts/raw/results.xml
            url = f"https://novgit05.novero.com/skateblack/CarIF/CarIF_SW/-/jobs/{id}/artifacts/raw/output.xml"
            urllib.request.urlretrieve(url, f'report/output{index + 1}.xml')

    def get_length_artifacts_id_list(self):
        return len(self.__artifact_id_list__)
