from django.test import TestCase#测试父类
from django.urls import resolve#解析网址
from .views import home_page
from django.http import HttpRequest
from .models import Item
# Create your tests here.

class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found=resolve('/')
        print(repr(found))
        self.assertEqual(found.func,home_page)

    def test_home_page_returns_correct_html(self):
        request=HttpRequest()
        response=home_page(request)#调用函数，检查响应的方法是永远可以使用的测试方法
        html=response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn("<title>To-Do lists</title>",html)
        self.assertTrue(html.endswith('</html>'))

    def test_uses_home_template(self):
        response=self.client.get('/')#使用client
        self.assertTemplateUsed(response,'home.html')

    def test_can_save_a_POST_request(self):
        response=self.client.post('/',data={'item_text':'a new list item'})

        self.assertEqual(Item.objects.count(),1,msg=f'items {Item.objects.count()}')
        new_item=Item.objects.first()#Item.objects.first()等价于Item.objects.all()[0]
        self.assertEqual(new_item.text,'a new list item')

        self.assertIn('a new list item',response.content.decode(),f'response content {response.content.decode()}')
        self.assertTemplateUsed(response,'home.html')

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response=self.client.get('/')

        self.assertIn('itemey 1',response.content.decode())
        self.assertIn('itemey 2',response.content.decode())






class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item=Item()#创建对象
        first_item.text='the first (ever) list item'#为对象赋值
        first_item.save()

        second_item=Item()
        second_item.text='item the second'
        second_item.save()

        saved_items=Item.objects.all()#查询数据库api，即类属性.objects
        self.assertEqual(saved_items.count(),2)

        first_saved_item=saved_items[0]
        second_saved_item=saved_items[1]
        print(first_saved_item)
        self.assertEqual(first_saved_item.text,'the first (ever) list item',f"first text {first_saved_item}")
        self.assertEqual(second_saved_item.text,'item the second')


