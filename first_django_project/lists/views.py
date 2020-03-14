from django.shortcuts import render,redirect
from django.http import request
from .models import Item,List
# Create your views here.视图函数用于处理请求-用户输入，返回适当响应

def home_page(request):
    # if request.method=='POST':
    #     list_item = List.objects.create()
    #     Item.objects.create(text=request.POST['item_text'], list=list_item)
    #     return redirect(f'/lists/{list_item.id}/')
    return render(request,'home.html')
    #第三个参数是要返回reaponse的时候给页面变量的赋值字典，"item_text"为input 标签的name

def new_list(request):
    list_item=List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_item)
    return redirect(f'/lists/{list_item.id}/')


def view_list(request,list_id):
    list_item=List.objects.get(id=list_id)#只显示id对应的列表
    items=Item.objects.filter(list=list_item)
    return render(request,'list.html',{'items':items,'list':list_item})

def add_item(request,list_id):
    list_item=List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'],list=list_item)
    return redirect(f'/lists/{list_item.id}/')

