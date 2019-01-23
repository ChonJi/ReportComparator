from selenium import webdriver
import requests

class DriverGetJobsId():
    def __init__(self, url="https://novgit05.novero.com/api/v4/projects/1134/jobs?private_token=oza_geyUkXm-iC8ZFxgx"):
        self.url = f"{url}&scope[]=success&scope[]=failed"

    def request_jobs(self, page=1):
        return requests.get(f"{self.url}&per_page=100&page={page}")

    def get_jobs(self):
        current_page=1
        while current_page >= 1:
            result = self.request_jobs(page=current_page)
            if result.status_code!=200:
                break
            for job in result.json():
                yield job
            current_page = result.get("next", -1)

    def get_job_ids_with_pipelines(self, max_jobs=100, pipeline=30000):
        artifacts = []
        i = 0
        for job in self.get_jobs():
            if job['stage'] != 'test' or job['name'] == 'SonarCube':
                continue
            pipeline_id = job['pipeline']['id']
            artifacts.append((job['id'], pipeline_id))
            if pipeline_id <= pipeline:
                break
            if i==max_jobs:
                break

        return artifacts