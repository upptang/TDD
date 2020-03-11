from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        '''
        在测试方法执行之前执行
        :return:
        '''
        self.browser=webdriver.Firefox()

    def tearDown(self):
        '''
        在测试方法执行之后执行，或者测试执行出错，也会执行
        :return:
        '''
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''
        以test_开头的方法都是测试方法，由测试运行程序运行，可以有多个
        :return:
        '''
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do',self.browser.title)

        self.fail('finish the test!')#都会失败，生成指定的错误信息，AssertionError:***


if __name__=='__main__':
    unittest.main()#启动unittest的测试运行程序