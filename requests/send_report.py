import requests

class TestClass:
    def test_send_report(self):
        token = "[paste your token here]"
        headers = {
            "Authorization": "Bearer " + token,
        }

        url = "https://api.zephyrscale.smartbear.com/v2/automations/executions/junit?projectKey=[paste your project key from jira]"
        report = {"file": open("[paste path to your xml report]", "rb")}

        r = requests.post(
            url,
            headers=headers,
            files=report)

        assert r.status_code == 200 or 201
