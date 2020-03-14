from selenium import webdriver
from selenium.webdriver.common.keys import Keys#Keys类，发送回车键等特殊按键
import unittest
import time

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

    def check_for_row_in_list_table(self,row_text):
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')
        inputbox.send_keys(row_text)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')#elements返回列表，可能为空列表，element返回元素，可能为none
        self.assertTrue(any(row.text==row_text for row in rows),f"new to-do item did not appear in table,contents were :\n{table.text}")
        #f字符串中可以使用{}插入局部变量，table.text



    def test_can_start_a_list_and_retrieve_it_later(self):
        '''
        以test_开头的方法都是测试方法，由测试运行程序运行，可以有多个
        :return:
        '''
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do',self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        self.check_for_row_in_list_table('1:buy peacock feathers')
        self.check_for_row_in_list_table('2:use peacock feathers to make a fly')

        self.fail('finish the test!')#都会失败，生成指定的错误信息，AssertionError:***




if __name__=='__main__':
    unittest.main()#启动unittest的测试运行程序