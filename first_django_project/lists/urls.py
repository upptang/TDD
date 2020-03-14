from django.conf.urls import url
from . import views
'''
lists应用对应的地址映射
'''

urlpatterns=[
url(r'^new$',views.new_list,name='new_list'),
    url(r'^(\d+)/$',views.view_list,name='view_list'),#（.+)正则表达式，用此方法解析，会向视图函数传递两个参数，request和正则表达式匹配的字符串
    url(r'^(\d+)/add_item$',views.add_item,name='add_item')
]