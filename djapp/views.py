from django.shortcuts import render,HttpResponse

# Create your views here.

def index(requests):
    context={
        "title":"测试数据模板"
    }
    return render(requests,"Books/login.html",context)

#新增数据
#方法一
# from  djapp.models import BookInfo
# book=BookInfo(
#     name="Djano",
#     pub_date='2000-1-1',
#     readcount=10
# )
# book.save()
#方法二 object
# BookInfo.objects.create(
#     name="测试开发入门",
#     pub_date='2000-1-1',
#     readcount=100
# )


# #修改数据
# #方式一
# book=BookInfo.objects.get(id=6)
# book.name='运维开发入门'
# book.save()
# #方式一
# BookInfo.objects.filter(id=6).update(name="运维开发入门",commentcount=6666)
# BookInfo.objects.filter(id=5).update(name="555",commentcount=999)

#删除数据
# book=BookInfo.objects.get(id=6).delete()
# book=BookInfo.objects.filter(id=6).delete()
