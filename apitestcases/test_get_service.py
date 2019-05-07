
from apicoreservices import api_lib
from apicoreservices.log_lib import Log

logging = Log.log_config()

class GetServiceTest(api_lib.ApiCore):

    def test_case1(self):
        '''
        verify that status code is 200
        '''
        assert self.get_stauscode() == 200
        logging.info(msg='Test_Case1 PASSED with {}'.format(self.get_stauscode()))

    def test_case2(self):
        '''
        verify the schema
        '''
        self.validate_json_schema('schema.json', 'list', response_json=self.get_json())
        logging.info(msg='Test Case2 PASSED Validated json {}'.format(self.get_json()))

    def test_case3(self):
        '''
        verify that API returns at least 100 records
        '''
        assert self.get_response_count() == 100
        logging.info(msg='Test Case3 PASSED with response count {}'.format(self.get_response_count()))

    def test_case4(self):
        '''
        verify that status code is 200 -> https://jsonplaceholder.typicode.com/posts/1
        '''
        assert self.get_stauscode() == 200
        logging.info(msg='Test_case4 PASSED Validated json {}'.format(self.get_json()))

    def test_case5(self):
        '''
        verify the schema -> https://jsonplaceholder.typicode.com/posts/1
        '''
        self.validate_json_schema('schema.json', 'dict', response_json=self.get_json())
        logging.info(msg='Test_Case5 PASSED Validated json {}'.format(self.get_json()))

    def test_case6(self):
        '''
        verify that API returns only one record so it has
        4 key value pairs -> https://jsonplaceholder.typicode.com/posts/1
        '''
        assert self.get_response_count() == 4
        logging.info(msg='Test_Case6 PASSED response count {}'.format(self.get_response_count()))

    def test_case7(self):
        '''
        verify that id in response matches the input (1) -> https://jsonplaceholder.typicode.com/posts/1
        '''
        assert self.get_json()['userId'] == 1
        logging.info(msg='Test_Case7 PASSED usedId  value is {}'.format(self.get_json()['userId'] ))

    def test_case8(self):
        '''
        verify that status code is 404 -> https://jsonplaceholder.typicode.com/invalidposts
        '''
        assert self.get_stauscode() == 404
        logging.info(msg='Test_Case8  {}'.format(self.get_stauscode()))