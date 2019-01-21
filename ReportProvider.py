import urllib.request

from DriverGetJobsId import DriverGetJobsId


class ReportProvider:
    __artifact_id_list__ = []

    def __init__(self):
        driver = DriverGetJobsId()
        self.__artifact_id_list__ = driver.test_build_job_id_list()[0:2]

        for index, id in enumerate(self.__artifact_id_list__):
            url = f"https://gitlab.com/ChonJi1983/TestRun/-/jobs/{self.__artifact_id_list__[index]}/artifacts/raw/results.xml"
            urllib.request.urlretrieve(url, f'report/output{index + 1}.xml')

    def get_length_artifacts_id_list(self):
        return len(self.__artifact_id_list__)