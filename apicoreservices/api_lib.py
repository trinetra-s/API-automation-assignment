import requests
import json
import jsonschema
import os


class ApiCore():

    def __init__(self, url):
        self.data = requests.get(url)

    def get_stauscode(self):
        return self.data.status_code

    def get_json(self):
        return self.data.json()

    def get_response_count(self):
        return len(self.get_json())

    def validate_json_schema(self, json_schema, type):
        dir = os.path.abspath(os.path.join('schema', json_schema))
        try:
            with open(dir, 'rb') as f:
                f_data = f.read().decode('utf-8')
            data = self.get_json()
        except FileNotFoundError as e:
            print('File Not Found!!!', e)
        try:
            if type == 'list':
                type = data[0]
            if type == 'dict':
                type = data
            jsonschema.validate(instance= type, schema= json.loads(f_data))
        except jsonschema.exceptions.ValidationError as e:
            print('The JSON is invalid', e)

    def create_data(self, url, data, headers):
        response = requests.post(url, data, headers)
        return response

    def update_data(self, url, data, headers):
        response = requests.put(url, data, headers= headers)
        return response

    def delete_data(self, url, headers):
        response = requests.delete(url, headers=headers)
        return response

