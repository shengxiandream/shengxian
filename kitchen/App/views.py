import hashlib
import random
import re

from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from App.models import User, Type, Good, shipping
from django.conf import settings


def indexi(request):
    # def index(request):
    #     type = Type.objects.all()
    #     Sp = Good.objects.all()
    #     return render(request, 'index.html', context={
    #         'type': type,
    #         'sp': Sp,
    #     })
    # type = Type.objects.all()
    # sp = Good.objects.all()
    if request.method == 'GET':
        return render(request, 'logini.html')

    if 'uid' in request.session:

        username = request.session.get('username')

        return render(request, "indexi.html")

    # return render(request, "login.html")
    # def index1(request):
    #     type = Type.objects.all()
    #     Sp = Good.objects.all()
    #     username = request.session['username']
    #     return render(request, 'index.html', context={
    #         'type': type,
    #         'sp': Sp,
    #         'username': username})



#登录
#加验证码
def logini(request):
    type = Type.objects.all()
    Sp = Good.objects.all()
    if request.method == 'GET':
        return render(request, 'logini.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 对密码进行sha1签名
        password = hashlib.sha1(password.encode('utf8')).hexdigest()
        #查询数据库
        res = User.objects.filter(username=username,password=password).values('username','id')
        if len(res) > 0:
            request.session['uid'] = res[0]['id']
            request.session['username'] = username
            request.session.set_expiry(600)   #过期时间 多少秒过期
            return render(request, 'indexi.html', context={
                'username': username,
                'type': type,
                'sp': Sp,})
        else:
            return render(request, 'logini.html')






def register(request):
    if request.method == 'POST':
        a = 0
        b = 0
        c = 0
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        res = User.objects.all()
        # print('aaaaaa',res)
        # print('aaaaaaa',res)
        if not username:
            a = 1
        # elif username in res[0].username:
        elif User.objects.filter(username=username):
            a = 2
        elif not email:
            b = 1
        elif not re.match(r'^(\w{3,15})@(\w{2,5})\.(com|cn|net)$',str(email)):
            b = 2
        elif User.objects.filter(email=email):
            b = 3
        elif not re.match(r'[\w]{8,18}$',str(password)):
            c = 1
        elif str(password).isdigit():
            c = 2
        else:
            password = hashlib.sha1(password.encode('utf8')).hexdigest()
            user = User(username=username,password=password,email=email,phone=phone)
            user.save()
            request.session['username'] = username
            request.session['email'] = email
            request.session['password'] = password
        if a > 0 or b > 0 or c > 0:
            return render(request,'register.html',context={
                'a':a,
                'b':b,
                'c':c
            })
        else:
            return render(request, 'logini.html', context={
                'username':username
            })
        #     return render(request, 'index_home.html')
    else:
        return render(request, 'register.html')


#注销
def logout(request):
        request.session.flush()
        return render(request, 'logini.html')







#支付订单
#购物车结算--->提交订单
def placeorder(request):
    return render(request,'place_order.html')


#全部订单
#我的订单-->全部订单   #点击我的订单默认跳转到全部订单
def order(request):
    return render(request,'user_center_order.html')
#去支付
# 支付界面
def orders(request):
    return render(request,'place_order.html')

#用户中心
#大标题用户中心
#标题我的订单-->个人信息
def info(request):
    username = request.session.get('username')
    print(username)
    set = User.objects.filter(username=username)
    print(set)
    city = set[0].city
    email = set[0].email
    phone = set[0].phone
    sex = set[0].sex
    age = set[0].age
    birthday = set[0].birthday
    # phone = set[0].phone
    return render(request,'user_center_info.html',context={
        'city':city,
        'email':email,
        'phone':phone,
        'sex':sex,
        'age':age,
        'birthday':birthday,
    })

#收货地址
#我的订单---->收货地址
def site(request):
    if request.method == 'GET':

        username = request.session.get('username')
        set = User.objects.filter(username=username)
        citylist = set[0].city
        return render(request,'user_center_site.html',context={
            'city':citylist
        })
    if request.method == 'POST':
        username = request.POST.get('username')
        site = request.POST.get('site')
        phone = request.POST.get('phone')
        username = request.session.get('username')
        set = User.objects.filter(username=username)
        uid = set[0].id
        ret = shipping()
        ret.username = username
        ret.id = uid
        ret.site = site
        ret.phone = phone
        ret.save()
        return render(request,'user_center_info.html')


#商品信息
#首页点击商品跳转商品首页
def detail(request,goodid):

    # username = request.POST.get('username')
    good = Good.objects.get(id=goodid)
    # goods_name = Good.objects.get(id=goodid)
    # set = Good.objects.filter(id = goodid)
    # stock = set[0].kucun
    # price = set[0].price
    # num = 1


    return render(request,'detail.html',context={
        'good':good,
        # 'goods_name':goods_name,
        # 'stock':stock,
        # 'price':price,
        # 'num':num,
    })

# 查询
def check(request):
    if request.method == 'POST':
        ret = request.POST.get('check')
        print(ret)
        good = Good.objects.filter(name__contains=ret)
        # books = Book.objects.filter(Q(ISBN__icontains=q)| Q(bookname__icontains=q)).order_by('-year')
        # pic = good[0].pic
        # name = good[0].name
        # price = good[0].price
        let = good.exists()
        if let:
            return render(request, 'check.html', context={
                'good':good
                # 'name': name,
                # 'price':price,
                # 'pic':pic
            })
        else:
            a = '没有你要搜索的而商品'
            return render(request,'check.html',context={
                'a':a
            })
    else:
        return render(request, 'indexi.html')




    #     print(good)
    #     if len(good):
    #         return render(request, 'detail.html', context={
    #             'good': good,
    #         })
    # return render(request,'login.html')

#修改个人信息
def change(request):
    if request.method == 'GET':
        return render(request,'change.html')
    if request.method == 'POST':
        username = request.session.get('username')
        city = request.POST.get('city')
        # password = request.POST.get('password')
        # password2 = request.POST.get('password2')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        sex = request.POST.get('sex')
        age = request.POST.get('age')

        set = User.objects.filter(username=username)
        set.update(city=city,email=email,phone=phone,sex=sex,age=age)
        print(set)
        return render(request,'xiugai.html')


 # 修改密码
def password(request):
    if request.method == 'POST':
        username = request.session.get('username')
        password = request.POST.get('password')
        print(password)
        password1 = hashlib.sha1(password.encode('utf8')).hexdigest()
        print(password1)
        password2 = request.POST.get('password2')
        password3 = request.POST.get('password3')
        set = User.objects.filter(username=username)
        password4 = set[0].password
        print(password4)
        if password1 != password4:
            a = '密码不正确'
        elif password3 !=password2:
            a = '两次密码不正确'
        elif not re.match(r'[\w]{8,18}$', str(password)):
            a = '密码为不小于8位数的数字加字母'
        elif str(password).isdigit():
            a = '密码不能为纯数字'
        else:
            set = User.objects.filter(username=username)
            password2 = hashlib.sha1(password2.encode('utf8')).hexdigest()
            set.update(password=password2)
            return render(request,'user_center_info.html')
        if a:
            return render(request,'password.html',context={
                'a':a,
            })
    else:
        return render(request,'password.html')


#找回密码
#登录界面
#加手机验证

#发送邮件
def send(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        # print(username)
        set = User.objects.filter(username=username)
        email = str(set[0].email)
        # print(email)
        # print('sdsadadadasdsadsadasdasd',set)
        if set:
            yan = random.randint(100000, 999999)
            request.session['username'] = username
            request.session['yan'] = yan
            request.session.set_expiry(2000)
            yzm = request.session.get('yan')
            print('123456dsasadadadada', yzm)
            subject, from_email, to = 'html', settings.EMAIL_HOST_USER, [email]
            html_content = render(request, 'email.html', context={
                'username': username,
                'yzm': yan
            }).content
            content = html_content.decode('utf8')
            print(content)
            mail = EmailMultiAlternatives(subject=subject, from_email=from_email, to=to)
            mail.attach_alternative(content, 'text/html')
            mail.send()
            return HttpResponse("html邮件")
    else:
        return render(request, 'passwords.html')


#找回密码
def passwords(request):

    if request.method == "POST":
        username = request.POST.get('username')
        set = User.objects.filter(username=username).exists()
        username = request.session.get('username')
        password = request.POST.get('password')     #POST写错写为session #粗心大意错误找了半天！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        print('dadadadadada',username)              #在遇见简单代码不可理解耐人匪夷所思的错误仔细看自己的代码流程
        print('dadadadadadadsadasd',password)
        yzm = str(request.session.get('yan'))
        print (type(yzm),'dadadddadada',yzm)
        yzm1 = str(request.POST.get('yzm'))
        print(type(yzm1),'dadadadadadadada',yzm1)

        if not set:
            b = '用户名不存在'
            return render(request, 'passwords.html', context={
                'b': b
            })
        elif yzm != yzm1:
            a = '验证码错误'
            return render(request, 'passwords.html', context={
                'a': a
            })
        elif not re.match(r'[\w]{8,18}$', str(password)):
            c = '密码为不小于8位数的数字加字母'
            return render(request, 'passwords.html', context={
                'c': c
            })
        elif str(password).isdigit():
            d = '密码不能为纯数字'
            return render(request, 'passwords.html', context={
                'd': d
            })
        else:
            zet = User.objects.filter(username=username)
            password2 = hashlib.sha1(password.encode('utf8')).hexdigest()
            print(password2)
            zet.update(password=password2)
            # zet.password=password2
            # zet.save()
            return render(request, 'logini.html')
    else:
        return render(request,'passwords.html')



# 我的购物车
def cart(request):

    # good = Good.objects.get(id=goodsid)

    return render(request, 'cart.html')

#商品信息
#商品数量的增加
#与总价的增加
def addgood(request):
    return None


#商品数量增加
#与总价的增加
def addcart(request):
    return None



# def gougou(request):
#     data = {
#         'status': '200',
#     }
#
#     # 获取js中回调函数(getjson)
#     # 传过来的参数
#
#     goodsid = request.get.get('goodsid')
#     register_id = request.session.get('register_id')
#
#     if not register_id:
#         data['status'] = '777'
#     else:
#
#     goods = cartmodel.objects.filter(userid=register_id).filter(goodsid=goodsid)
#     if goods.exists():
#         good = goods.first()
#     good.c_num = good.c_num + 1
#
#     good.save()
#     data['num'] = good.c_num
#     else:
#     good = cartmodel()
#     good.userid_id = register_id
#     good.goodsid_id = goodsid
#     good.c_num = 1
#
#     good.save()
#     data['num'] = good.c_num
#     return jsonresponse(data)
#
#
#     return render(request,'gougou.html',context={
#
#     })


def list(request):
    return render(request,'list.html')