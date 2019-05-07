import sys
import os
import pytest
sys.path.append(os.getcwd())
from apitestcases.test_get_service import GetServiceTest
from apitestcases.test_post_service import PostServiceTest
from apitestcases.test_put_service import PutServiceTest
from apitestcases.test_delete_service import DeleteServiceTest


class TestRunner():

    def test_get_service(self):
        get_test1 = GetServiceTest('https://jsonplaceholder.typicode.com/posts')
        get_test1.test_case1()
        get_test1.test_case2()
        get_test1.test_case3()

        get_test2 = GetServiceTest('https://jsonplaceholder.typicode.com/posts/1')
        get_test2.test_case4()
        get_test2.test_case5()
        get_test2.test_case6()
        get_test2.test_case7()

        get_test3 = GetServiceTest('https://jsonplaceholder.typicode.com/invalidposts')
        get_test3.test_case8()

    def test_post_service(self):
        post_test = PostServiceTest('https://jsonplaceholder.typicode.com/posts')
        post_test.test_case1()
        post_test.test_case2()
        post_test.test_case3()
    
    def test_put_service(self):
        put_test = PutServiceTest('https://jsonplaceholder.typicode.com/posts/1')
        put_test.test_case1()
        put_test.test_case2()
        put_test.test_case3()

    def test_delete_service(self):
        delete_test = DeleteServiceTest('https://jsonplaceholder.typicode.com/posts/1')
        delete_test.test_case1()
        delete_test.test_case2()
        delete_test.test_case3()

if __name__ == '__main__':
   pytest.main()



