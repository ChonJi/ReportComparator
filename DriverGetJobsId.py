from selenium import webdriver


class DriverGetJobsId():
    __page__ = 'https://gitlab.com/ChonJi1983/TestRun/-/jobs'

    def test_build_job_id_list(self):

        list_artifacts = []

        driver = webdriver.Chrome(executable_path=r"driver\chromedriver.exe")
        driver.maximize_window()
        driver.get(self.__page__)

        list_of_stages = driver.find_elements_by_xpath('//tbody/tr/td[4]')

        for index, stage in enumerate(list_of_stages):

            if driver.find_element_by_xpath(f"//tbody/tr[{index + 1}]/td[4]").text == 'test':
                element = driver.find_element_by_xpath(f"(//tbody//span[@class = 'build-link'])[{index + 1}]").text[1:]
                list_artifacts.append(element)

        driver.quit()
        return list_artifacts