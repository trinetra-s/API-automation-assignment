from apicoreservices import api_lib
import logging

class TestPutService(api_lib.ApiCore):

    def test_case1(self):
        '''
        Update a resouce at 'https://jsonplaceholder.typicode.com/posts/1'
        '''
        header = {"Content-type": "application/json",
                  "charset": "UTF-8",
                  }
        url = 'https://jsonplaceholder.typicode.com/posts/1'
        payload = {"id" : 1,
                   "title" : "abc",
                   "body": "xyz",
                   "userId" : 1
                   }
        return  self.update_data(url, data=payload, headers=header)

    def test_case2(self):
        res_status_code = self.test_case1().status_code
        if res_status_code == 200:
            logging.info(msg='Update is successfull{}'.format(res_status_code))
        else:
            logging.critical(msg='Update is unsuccessfull {}'.format(res_status_code))

    def test_case3(self):
        '''
        Verify schema after put call.
        '''
        self.validate_json_schema('schema.json', 'dict')