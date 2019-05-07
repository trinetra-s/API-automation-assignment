from apicoreservices import api_lib
from apicoreservices.log_lib import Log

class DeleteServiceTest(api_lib.ApiCore):

    logging = Log.log_config()

    def test_case1(self):
            '''
            Delete the resource at end-point https://jsonplaceholder.typicode.com/posts/1
            '''
            url = 'https://jsonplaceholder.typicode.com/posts/1'
            header = {"Content-type": "application/json",
                      "charset": "UTF-8",
                      "Accept": "text/plain"}
            data = self.delete_data(url, headers=header)
            return data

    def test_case2(self):
            '''
            Verifying the status code after deleting the resource.
            '''
            assert self.test_case1().status_code == 200
            self.logging.info('TEST CASE2 PASSED and resource deleted {}'.format(self.test_case1().status_code))

    def test_case3(self):
            '''
            Verifying the response should return an empty dict indicating
            the resource is deleted.
            '''
            assert self.test_case1().json() == {}
            self.logging.info('TEST CASE3 PASSED and resource deleted {}'.format(self.test_case1().json()))

