from apicoreservices import api_lib
import json
from apicoreservices.log_lib import Log

class PostServiceTest(api_lib.ApiCore):

    logging = Log.log_config()

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
        data = self.create_data(url, body_string, header)
        self.logging.info('TEST CASE1 PASSED and resource accepted{}'.format(data.status_code))
        return data


    def test_case2(self):
        '''
        Verify the status code is 201 to check if the resource is created on server end.
        '''
        assert self.test_case1().status_code == 201

    def test_case3(self):
        '''
        Verify schema after post call. by reading the response via GET method.
        '''
        self.validate_json_schema('schema.json', 'list', response_json=self.get_json())
        self.logging.info(msg='Test Case2 PASSED Validated json {}'.format(self.get_json()))



