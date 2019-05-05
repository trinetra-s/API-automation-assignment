from apicoreservices import api_lib
import json

class TestPostService(api_lib.ApiCore):

    def test_case1(self):
        header = {"Content-type": "application/json",
                  "charset": "UTF-8",
                  "Accept": "text/plain"}
        url = 'https://jsonplaceholder.typicode.com/posts'
        body = {"title": "foo",
                "body": "bar",
                "id": 101,
                "userId": 10}
        body_string = json.dumps(body)
        return self.create_data(url, body_string, header)


    def test_case2(self):
        '''
        Verify the status code is 201 to check if the resource is created on server end.
        '''
        assert self.test_case1().status_code == 201

    def test_case3(self):
        '''
        Verify schema after post call.
        '''
        response = self.get_json()
        self.validate_json_schema('schema.json', 'list')



