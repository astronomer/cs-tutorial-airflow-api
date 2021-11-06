import requests
import json
import pandas as pd
from requests.auth import HTTPBasicAuth

class AirflowAPI:
    def __init__(self):
        self.domain = 'http://localhost:8080'
        self.headers = {
            "cache-control": "no-cache",
            "content-type": "application/json",
            "accept": "application/json",
        }
        self.auth = HTTPBasicAuth('admin', 'admin')

    def _toggle_pause(self, dag_id, is_paused):
        endpoint = f'/api/v1/dags/{dag_id}'
        url = self.domain + endpoint
        payload = {
            "is_paused": is_paused
        }
        response = requests.patch(url=url, headers=self.headers, data=json.dumps(payload), auth=self.auth).json()
        print(response)

    def _get_dags(self):
        response = self._get_request(endpoint='/api/v1/dags')
        print(response)

    def _get_dag_runs(self, dag_id):
        response = self._get_request(endpoint=f'/api/v1/dags/{dag_id}/dagRuns')
        df = pd.json_normalize(response, record_path=['dag_runs'])
        df.to_csv("out.csv", index=False)

    def _get_task_instances(self):
        url = self.domain + '/api/v1/dags/~/dagRuns/~/taskInstances/list'
        payload = {}
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload), auth=self.auth).json()
        df = pd.json_normalize(response, record_path=['task_instances'])
        df.to_csv("out.csv", index=False)

    def _get_roles(self):
        response = self._get_request(endpoint='/api/v1/roles')
        print(response)
        return response

    def _get_role(self, role_name):
        response = self._get_request(endpoint=f'/api/v1/roles/{role_name}')
        print(response)
        return response

    def _copy_role(self, role_name, from_role):
        url = self.domain + f"/api/v1/roles"
        payload = self._get_role(role_name=from_role)
        new_role = {'name': role_name}
        payload.update(new_role)
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload), auth=self.auth)
        print(f"{response.status_code} - {response.reason}")

    def _delete_role(self, role_name):
        url = self.domain + f"/api/v1/roles/{role_name}"
        response = requests.delete(url=url, headers=self.headers, auth=self.auth)
        print(f"{response.status_code} - {response.reason}")

    def _create_role(self, role_name):
        url = self.domain + "/api/v1/roles"
        payload = {
            "name": role_name,
            "actions": []
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload), auth=self.auth)
        print(f"{response.status_code} - {response.reason}")

    def _update_role(self, role_name):
        url = self.domain + f"/api/v1/roles/{role_name}"
        with open(f'airflow_custom_roles/{role_name}.json') as f:
            payload = json.load(f)
        response = requests.patch(url=url, headers=self.headers, data=json.dumps(payload), auth=self.auth)
        print(f"{response.status_code} - {response.reason}")

    def _get_request(self, endpoint):
        url = self.domain + endpoint
        response = requests.get(url=url, headers=self.headers, auth=self.auth).json()
        return response

if __name__ == '__main__':
    A = AirflowAPI()
