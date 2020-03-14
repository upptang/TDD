from django.db import models

# Create your models here.

class List(models.Model):
    pass

class Item(models.Model):#继承了models.Model，使得这个类可以映射成表，会自动生成id属性，作为表的主键，其他列得自己定义
    text=models.TextField(default='')#定义text属性对应表中的text列,迁移时不可以添加没有默认值的列
    list=models.TextField(List,default=None)#外键