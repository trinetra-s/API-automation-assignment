
from apicoreservices import api_lib


class TestGetService(api_lib.ApiCore):

    def test_case1(self):
        '''
        verify that status code is 200
        '''
        assert self.get_stauscode() == 200

    def test_case2(self):
        '''
        verify the schema
        '''
        self.validate_json_schema('schema.json', 'list')

    def test_case3(self):
        '''
        verify that API returns at least 100 records
        '''
        assert self.get_response_count() == 100

    def test_case4(self):
        '''
        verify that status code is 200 -> https://jsonplaceholder.typicode.com/posts/1
        '''
        assert self.get_stauscode() == 200

    def test_case5(self):
        '''
        verify the schema -> https://jsonplaceholder.typicode.com/posts/1
        '''
        self.validate_json_schema('schema.json', 'dict')

    def test_case6(self):
        '''
        verify that API returns only one record so it has
        4 key value pairs -> https://jsonplaceholder.typicode.com/posts/1
        '''
        assert self.get_response_count() == 4

    def test_case7(self):
        '''
        verify that id in response matches the input (1) -> https://jsonplaceholder.typicode.com/posts/1
        '''
        assert self.get_json()['userId'] == 1

    def test_case8(self):
        '''
        verify that status code is 404 -> https://jsonplaceholder.typicode.com/invalidposts
        '''
        assert self.get_stauscode() == 404