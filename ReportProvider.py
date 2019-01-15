import requests
import urllib.request

class ReportProvider:

    def __init__(self, artifact_id):
        url = f"https://gitlab.com/ChonJi1983/TestRun/-/jobs/{artifact_id}/artifacts/raw/results.xml"
        urllib.request.urlretrieve(url, 'actual_report.xml')















