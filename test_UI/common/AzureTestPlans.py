import json
import requests
import datetime
from config.SetUIConfig import Platform, Target, Project, Env

organization_url = "https://dev.azure.com/JTI-RD/"
personal_access_token = 'wukpblkgcadcc6i37yzialz46betricja2oexflv7tks5wk6xara'
projectName = "CaiLiFang"
headers = {'Content-Type': 'application/json'}


class AzureTestPlan(object):

    def query_point_id(self, planID, suitesID, caseID):
        global organization_url, personal_access_token, projectName, headers

        url = organization_url + projectName + "/_apis/test/Plans/" + str(planID) + "/Suites/" + str(
            suitesID) + "/points?testCaseId=" + str(caseID) + "&api-version=5.1"
        res = requests.get(url, headers=headers, auth=(personal_access_token, personal_access_token))
        json_array = res.json()
        testPoint = json_array['value'][0]['id']
        print(testPoint)
        return testPoint

    def add_test_status(self, runID, planID):
        global organization_url, personal_access_token, projectName, headers

        testresults = [{
            "testRun": str(runID),
            "testPlan": {
                "id": str(planID)
            },
            "testCaseTitle": "彩票列表可導入正確彩種",
            "TestPointId": 37,
            "priority": 2,
            "outcome": "Passed",
        }]

        url = organization_url + projectName + "/_apis/test/Runs/" + str(runID) + "/results?api-version=5.1"
        res = requests.post(url, data=json.dumps(testresults), headers=headers,
                            auth=(personal_access_token, personal_access_token))
        print(res.status_code)
        print(res.text)

    def update_test_status(self, runID, planID, suiteID, caseID, result):
        global organization_url, personal_access_token, projectName, headers

        # pass
        testPoint = self.query_point_id(planID, suiteID, caseID)
        casePriority = self.query_test_case(planID, suiteID, caseID)
        resultID = self.get_result_id(runID, testPoint)

        status = ""
        if result == 0:
            status = "Passed"
        elif result == 1:
            status = "Failed"

        testresults = [{
            "id": resultID,
            "priority": casePriority,
            "state": "Completed",
            "outcome": status,
            "comment": "Platform: " + Platform + ", Target: " + Target + ", Env: " + Env + ", Project: " + Project
        }]

        url = organization_url + projectName + "/_apis/test/Runs/" + str(runID) + "/results?api-version=5.1"
        res = requests.patch(url, data=json.dumps(testresults), headers=headers,
                             auth=(personal_access_token, personal_access_token))
        print(res.status_code)
        print(res.text)

    def query_result_list(self, runID):
        global organization_url, personal_access_token, projectName, headers

        url = organization_url + projectName + "/_apis/test/Runs/" + str(runID) + "/results?api-version=5.1"
        res = requests.get(url, headers=headers, auth=(personal_access_token, personal_access_token))
        print(res.status_code)
        print(res.text)

    def get_result_id(self, runID, testPoint):
        global organization_url, personal_access_token, projectName, headers

        url = organization_url + projectName + "/_apis/test/Runs/" + str(runID) + "/results?api-version=5.1"
        res = requests.get(url, headers=headers, auth=(personal_access_token, personal_access_token))
        json_array = res.json()
        data = json_array['value']

        count = 0
        for item in data:
            if item['testPoint']['id'] == str(testPoint):
                break
            count += 1

        test_result_id = json_array['value'][count]['id']
        return test_result_id

    def create_test_run(self, planID, suiteID):
        global organization_url, personal_access_token, projectName, headers

        # pass
        pointID = self.query_test_suite(planID, suiteID)
        createTime = datetime.datetime.today()
        runName = Platform + '_' + Target + '_' + Project + '_' + Env + '_' + createTime.strftime("%Y%m%d%H%M")

        testresults = {
            "name": runName,
            "automated": True,
            "plan": {
                "id": str(planID)
            },
            "pointIds": pointID
        }

        url = organization_url + projectName + "/_apis/test/runs?api-version=5.1"
        res = requests.post(url, data=json.dumps(testresults), headers=headers,
                            auth=(personal_access_token, personal_access_token))
        data = res.json()
        print(data['id'])
        return data['id']

    def update_test_run(self, runID):
        global organization_url, personal_access_token, projectName, headers

        createTime = datetime.datetime.today()
        runName = createTime.strftime("%Y%m%d%H%M")

        testresults = {
            "state": "Completed",
        }

        url = organization_url + projectName + "/_apis/test/runs/" + str(runID) + "?api-version=5.1"
        res = requests.patch(url, data=json.dumps(testresults), headers=headers,
                             auth=(personal_access_token, personal_access_token))
        print(res.text)

    def query_test_run(self, planID):
        global organization_url, personal_access_token, projectName, headers

        url = organization_url + projectName + "/_apis/test/runs/?planIds=" + str(planID) + "api-version=5.1"
        res = requests.get(url, headers=headers, auth=(personal_access_token, personal_access_token))
        data = res.json()
        print(data[id])

    def query_test_suite(self, planID, suiteID):
        global organization_url, personal_access_token, projectName, headers

        url = organization_url + projectName + "/_apis/test/Plans/" + str(planID) + "/suites/" + str(suiteID) + \
            "/points?api-version=5.1"
        res = requests.get(url, headers=headers, auth=(personal_access_token, personal_access_token))
        json_array = res.json()
        data = json_array['value']

        pointID = []
        for item in data:
            pointID.append(item['id'])

        print(pointID)
        return pointID

    def query_test_case(self, planID, suiteID, caseID):
        global organization_url, personal_access_token, projectName, headers

        url = organization_url + projectName + "/_apis/testplan/Plans/" + str(planID) + "/Suites/" + str(suiteID) + \
            "/TestCase/" + str(caseID) + "?witFields=Priority&api-version=5.1-preview.2"
        res = requests.get(url, headers=headers, auth=(personal_access_token, personal_access_token))
        data = res.json()
        casePriority = data['value'][0]['workItem']['workItemFields'][0]['Priority']
        print(casePriority)
        return casePriority


if __name__ == '__main__':
    pass

