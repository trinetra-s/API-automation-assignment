from apicoreservices import api_lib
from apicoreservices.log_lib import Log


class PutServiceTest(api_lib.ApiCore):

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
        data = self.update_data(url, data=payload, headers=header)
        return data

    def test_case2(self):

        logging = Log.log_config(userLevel=40)
        res_status_code = self.test_case1().status_code
        if res_status_code == 200:
            logging.info(msg='Update is successfull{}'.format(res_status_code))
        else:
            logging.error(msg='Update is unsuccessfull {}'.format(res_status_code))
            raise AssertionError('The post call is unsuccessfull {}'.format(res_status_code))

    def test_case3(self):
        '''
        Verify schema after put call.
        Note : This validates the original json as the PUT call on
        https://jsonplaceholder.typicode.com/posts/1 fails with 500 internal server error
        '''
        self.validate_json_schema('schema.json', 'dict', response_json=self.get_json())