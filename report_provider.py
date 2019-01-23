import requests

from DriverGetJobsId import DriverGetJobsId


class ReportProvider:
    __artifact_id_list__ = []

    def __init__(self):
        driver = DriverGetJobsId()
        self.__artifact_id_list__ = driver.get_job_ids_with_pipelines(pipeline=23552)
        #shutil.rmtree('/report', ignore_errors=True)
        #os.mkdir('report')
        for index, (job_id, pipeline) in enumerate(self.__artifact_id_list__):
        #" 4Rfsax-rdMN5Cpmiym6Z  oza_geyUkXm-iC8ZFxgx   id project 1134
            url = f"https://novgit05.novero.com/api/v4/projects/1134/jobs/{job_id}/artifacts/Reports/output.xml?private_token=oza_geyUkXm-iC8ZFxgx"
            r = requests.get(url)
            if r.status_code!=200:
                print(f"Job: {job_id} from pipeline: {pipeline} failed to return artifacts")
                continue
            with open(f'report/output{pipeline}.xml', 'w',  encoding='utf-8') as f:
                f.write(r.text)

    def get_length_artifacts_id_list(self):
        return len(self.__artifact_id_list__)
