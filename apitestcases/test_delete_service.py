from apicoreservices import api_lib

class TestDeleteService(api_lib.ApiCore):

    def test_case1(self):
            '''
            Delete the resource at end-point https://jsonplaceholder.typicode.com/posts/1
            '''
            url = 'https://jsonplaceholder.typicode.com/posts/1'
            header = {"Content-type": "application/json",
                      "charset": "UTF-8",
                      "Accept": "text/plain"}
            return self.delete_data(url, headers=header)

    def test_case2(self):
            '''
            Verifying the status code after deleting the resource.
            '''
            assert self.test_case1().status_code == 200

    def test_case3(self):
            '''
            Verifying the response should return an empty dict indicating
            the resource is deleted.
            '''
            assert self.test_case1().json() == {}

