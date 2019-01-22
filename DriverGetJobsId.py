from selenium import webdriver


class DriverGetJobsId():
    __page__ = 'https://gitlab.com/ChonJi1983/TestRun/-/jobs'

    def build_job_id_list(self):

        list_artifacts = []

        self.driver = webdriver.Chrome(executable_path=r"driver\chromedriver.exe")
        driver = self.driver
        driver.maximize_window()
        driver.get(self.__page__)

        list_of_stages = self.get_stages_list()

        for index, stage in enumerate(list_of_stages):

            if self.get_stage_by_row(index + 1) == 'test' and self.get_status_by_row(index + 1) not in (
                    'canceled', 'running'):
                list_artifacts.append(self.get_job_id_by_row(index + 1))

        driver.quit()
        return list_artifacts

    def get_stages_list(self):
        return self.driver.find_elements_by_xpath('//tbody/tr/td[4]')

    def get_stage_by_row(self, row):
        stage_element = self.driver.find_element_by_xpath(f'//tbody/tr[{row}]/td[4]')
        return stage_element.text

    def get_status_by_row(self, row):
        status_element = self.driver.find_element_by_xpath(f'//tbody/tr[{row}]/td[1]')
        return status_element.text

    def get_job_id_by_row(self, row):
        jobid_element = self.driver.find_element_by_xpath(f"(//tbody//span[@class = 'build-link'])[{row}]")
        return jobid_element.text[1:]

    def get_pipeline_by_row(self, row):
        pipeline_element = self.driver.find_element_by_xpath(f'//tbody/tr[{row}]/td[3]')
        return pipeline_element.text

    def get_name_by_row(self, row):
        name_element = self.driver.find_element_by_xpath(f'//tbody/tr[{row}]/td[5]')
        return name_element.text

    # Gets job branch name
    def get_refname_by_row(self, row):
        refname_element = self.driver.find_element_by_xpath(f'(//a[@class="ref-name"])[{row}]')
        return refname_element.text
