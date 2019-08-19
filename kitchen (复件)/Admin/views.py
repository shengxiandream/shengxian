import hashlib
from random import randint

import os

from datetime import datetime
from django.conf.global_settings import MEDIA_URL
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.urls import reverse

from Admin.forms import ZhHu, AddShang, XiaoGuan
from Admin.formss import ZhCe
from kitchen import settings
from kitchen.settings import NUMOFPAGE
from .models import User, Auser, Aplate, Good, Type



# Create your views here.

def login(request):
    if request.method == 'POST':
        us = request.POST.get('username')
        pa = request.POST.get('password')
        pas = hashlib.sha1(pa.encode('utf-8')).hexdigest()
        if Auser.objects.filter(name=us) and pas == Auser.objects.filter(name=us)[0].password:
            dbk = Aplate.objects.filter(aid=0)
            xbk = Aplate.objects.filter(aid__gte=1)
            request.session['username'] = us
            request.session.set_expiry(0)
            return render(request, 'index.html',
                          context={'dbk': dbk, 'xbk': xbk, 'ming': Auser.objects.filter(name=us)[0]})
            # return redirect('app:index')
        else:
            return render(request, 'tiao.html', context={'a': '账号或密码错误，请重新登陆。'})
    return render(request, 'login.html')


def zhaohui(request):
    if request.method == 'POST':
        form = ZhHu(request.POST)
        us = request.POST.get('name')
        uss = Auser.objects.filter(name=us)
        yan = request.POST.get('yzm')
        yan1 = request.session.get('yzm')
        # print('kkkkk',yan,type(yan),yan1,type(yan1))
        # print(uss)
        if uss and form.is_valid() and yan == str(yan1):
            us = form.cleaned_data['username']
            uss = Auser.objects.filter(name=us)
            p1 = form.cleaned_data['password1']
            pas = hashlib.sha1(p1.encode('utf-8')).hexdigest()
            uss[0].password = pas
            uss[0].save()
            return render(request, 'tiao1.html', context={'a': '密码已重设成功，返回首页登陆吧。'})
        if uss == [] or str(yan1) != yan:
            return render(request, 'tiao.html', context={'a': '用户名或验证码错误，请重新找回。'})
        else:
            return render(request, 'zhaohui.html', context={'form': form})
    else:
        form = ZhHu()
    # print(form)
    return render(request, 'zhaohui.html', context={'form': form})


def youjian(request):
    if request.method == 'POST':
        us = request.POST.get('name')
        print(us)
        res = Auser.objects.filter(name=us)
        print(',,,,,,', res)
        if res:
            # request.session['username'] = us
            # request.session.set_expiry(0)
            youxiang = str(res[0].email)
            print('lllllll', youxiang)
            import random
            yan = random.randint(100000, 999999)
            request.session['yzm'] = yan
            request.session.set_expiry(120)
            subject, emial_from, to = '验证码', settings.EMAIL_HOST_USER, [youxiang]
            content = render(request, 'youxiang.html', context={'shuzi': yan}).content
            content = content.decode('utf8')
            print(content)
            mail = EmailMultiAlternatives(subject=subject, from_email=emial_from, to=to)
            mail.attach_alternative(content, 'text/html')
            mail.send()
            return HttpResponse("html邮件")
    else:
        return redirect('admin:login')


def upload(request):
    if request.method == 'POST':
        form = AddShang(request.POST)
        # photo (tupian也是)是表单中文件上传的name
        # file = request.FILES.get('photo')
        file = request.FILES.get('tupian')
        fenlie = request.POST.get('fenlie')
        ming = request.POST.get('ming')
        jianjie = request.POST.get('jianjie')
        jinjia = request.POST.get('jinjia')
        shoujia = request.POST.get('shoujia')
        kucun = request.POST.get('kucun')
        xiangxi = request.POST.get('fuw')
        print(file, fenlie, ming, jianjie, jinjia, shoujia, kucun, xiangxi)
        # print('kkkk',file)
        # 文件路径
        # path = os.path.join(settings.MEDIA_ROOT,file.name)
        local_path = os.path.join(settings.UPLOAD_PATH, file.name)
        path = local_path.replace("\\", '/')
        # print(local_path)
        # #文件类型过滤
        ext = os.path.splitext(file.name)
        # print(ext)
        # print(len(ext))
        # print(ext[1])
        if len(ext) < 1 or not ext[1] in settings.ALLOWED_FILEEXTS:  # ALLOWED_FILEEXTS
            # return redirect(reverse('upload'))
            # return redirect('admin:upload')
            # print(settings.ALLOWED_FILEEXTS)
            # return HttpResponse('no')
            return render(request, 'tiao2.html', context={'a': '图片格式不对'})

        # 解决文件重名
        if os.path.exists(path):

            # 日期目录
            dir = datetime.today().strftime("%Y/%m/%d")
            # print('1',dir)
            dir = os.path.join(settings.UPLOAD_PATH, dir)  # settings.MEDIA_ROOT
            # print('2',dir)
            if not os.path.exists(dir):
                os.makedirs(dir)  # 递归创建目录
            # list.png
            file_name = ext[0] + datetime.today().strftime("%Y%m%d%H%M%S") + str(randint(1, 1000)) + ext[1] if len(
                ext) > 1 else ''
            path = os.path.join(dir, file_name).replace("\\", '/')  #
        # print(path , type(path))
        # ac = path
        # print('ac',ac)


        # 创建新文件
        with open(path, 'wb') as fp:
            # 如果文件超过2.5M,则分块读写
            if file.multiple_chunks():
                for block1 in file.chunks():
                    fp.write(block1)
            else:
                fp.write(file.read())
        # return redirect(reverse('index'))
        path = '/' + path
        print(path, type(path))
        kucu = int(kucun) * 1000
        print('kkkkk', kucu)

        if xiangxi:
            xiangx = xiangxi
        else:
            xiangx = '<p>便宜的时候不多了,快来剁手吧.</p>'
        print('dddd', xiangxi)
        goods = Good(name=ming, titleid=fenlie, pic=path, price=shoujia, costing=jinjia, kucun=kucu, content=jianjie,xq=xiangx)
        goods.save()
        return render(request, 'tiao2.html', context={'a': '上传成功'})

    return render(request, 'tiao1.html', context={'a': '请先登陆'})


def index(request, did, page=1):
    if request.session.get('username'):
        us = request.session.get('username')
        dbk = Aplate.objects.filter(aid=0)
        xbk = Aplate.objects.filter(aid__gte=1)
        # did = request.GET.get('did')
        if did == '7':
            shpi = Good.objects.filter(isDelete=1)
            fen = Type.objects.all()
            paginator = Paginator(shpi, NUMOFPAGE)
            page = int(page)
            pagination = paginator.page(page)
            # 3 自定义页码范围
            if paginator.num_pages > 10:
                # 如果当前页码-5小于0
                if page - 5 <= 0:
                    customRange = range(1, 11)
                elif page + 4 > paginator.num_pages:
                    customRange = range(paginator.num_pages - 9, paginator.num_pages + 1)
                else:
                    customRange = range(page - 5, page + 5)
            else:  # 页码总数小于10
                customRange = paginator.page_range

            return render(request, 'shangle.html',
                          context={'dbk': dbk, 'xbk': xbk, 'ming': Auser.objects.filter(name=us)[0],
                                   'shpi': pagination.object_list, 'fen': fen, 'pagerange': customRange,
                                   'pagination': pagination})
        if did == '8':
            form = AddShang()
            # print(form)
            return render(request, 'addshang.html',
                          context={'form': form, 'dbk': dbk, 'xbk': xbk, 'ming': Auser.objects.filter(name=us)[0]})
        if did == '9':
            return render(request, 'shangfen.html',context={'dbk': dbk, 'xbk': xbk, 'ming': Auser.objects.filter(name=us)[0]})
        if did == '11':
            shpi = Good.objects.filter(isDelete=0)
            fen = Type.objects.all()
            paginator = Paginator(shpi, NUMOFPAGE)
            page = int(page)
            pagination = paginator.page(page)
            # 3 自定义页码范围
            if paginator.num_pages > 10:
                # 如果当前页码-5小于0
                if page - 5 <= 0:
                    customRange = range(1, 11)
                elif page + 4 > paginator.num_pages:
                    customRange = range(paginator.num_pages - 9, paginator.num_pages + 1)
                else:
                    customRange = range(page - 5, page + 5)
            else:  # 页码总数小于10
                customRange = paginator.page_range

            return render(request, 'shangxiale.html',context={'dbk': dbk, 'xbk': xbk, 'ming': Auser.objects.filter(name=us)[0],'shpi': pagination.object_list, 'fen': fen, 'pagerange': customRange, 'pagination': pagination})
        if did == '13':
            return render(request, 'dingle.html',context={'dbk': dbk, 'xbk': xbk, 'ming': Auser.objects.filter(name=us)[0]})
        if did == '19':
            yonghu = User.objects.filter(login_type=1)
            paginator = Paginator(yonghu, NUMOFPAGE)
            page = int(page)
            pagination = paginator.page(page)
            # 3 自定义页码范围
            if paginator.num_pages > 10:
                # 如果当前页码-5小于0
                if page - 5 <= 0:
                    customRange = range(1, 11)
                elif page + 4 > paginator.num_pages:
                    customRange = range(paginator.num_pages - 9, paginator.num_pages + 1)
                else:
                    customRange = range(page - 5, page + 5)
            else:  # 页码总数小于10
                customRange = paginator.page_range

            return render(request, 'yongle.html',context={'dbk': dbk, 'xbk': xbk, 'ming': Auser.objects.filter(name=us)[0],'yonghu': pagination.object_list,'pagerange': customRange,'pagination': pagination})
        if did == '20':
            yonghu = User.objects.filter(login_type=0)
            paginator = Paginator(yonghu, NUMOFPAGE)
            page = int(page)
            pagination = paginator.page(page)
            # 3 自定义页码范围
            if paginator.num_pages > 10:
                # 如果当前页码-5小于0
                if page - 5 <= 0:
                    customRange = range(1, 11)
                elif page + 4 > paginator.num_pages:
                    customRange = range(paginator.num_pages - 9, paginator.num_pages + 1)
                else:
                    customRange = range(page - 5, page + 5)
            else:  # 页码总数小于10
                customRange = paginator.page_range

            return render(request, 'yongxiale.html',context={'dbk': dbk, 'xbk': xbk, 'ming': Auser.objects.filter(name=us)[0],'yonghu': pagination.object_list,'pagerange': customRange,'pagination': pagination})
        if did == '21':
            return render(request, 'pinglun.html',
                          context={'dbk': dbk, 'xbk': xbk, 'ming': Auser.objects.filter(name=us)[0]})
        if did == '38':
            if request.method == 'POST':
                form = ZhCe(request.POST)
                if form.is_valid():
                    p1 = form.cleaned_data['password1']
                    us = form.cleaned_data['username']
                    em = form.cleaned_data['email']
                    lx = form.cleaned_data['typee']
                    pas = hashlib.sha1(p1.encode('utf-8')).hexdigest()
                    ause = Auser(name=us, password=pas, email=em, type=lx)
                    ause.save()
                    return render(request, 'tiao.html', context={'a': '注册成功'})
                else:
                    return render(request, 'zhuce.html', context={'form': form, 'dbk': dbk, 'xbk': xbk,
                                                                  'ming': request.session.get('username')})

            else:
                form = ZhCe()
                return render(request, 'zhuce.html',
                              context={'form': form, 'dbk': dbk, 'xbk': xbk, 'ming': request.session.get('username')})
        if did == '39':
            form = XiaoGuan()
            return render(request, 'xiaoguan.html',context={'form': form, 'dbk': dbk, 'xbk': xbk, 'ming': Auser.objects.filter(name=us)[0]})

    else:
        return redirect('admin:login')


        # def fu(request):
        #     if request.method == 'POST':
        #         da= request.POST.get('fuw')
        #         print(da)
        #         return render(request, 'fu.html')
        #     return render(request, 'fu.html')


        # def index(request):
        #     if request.method == 'POST':
        #         dbk=Aplate.objects.filter(aid=0)
        #         xbk = Aplate.objects.filter(aid__gte=1)
        #         us = request.session.get('username')
        #         print('kkkk',dbk)
        #         print('dddd',xbk)
        #         return render(request, 'index.html',context={'dbk':dbk,'xbk':xbk,'ming':us})
        #     else:
        #         return render(request, 'login.html')


def jinyong(request):
    if request.method == 'POST':
        cid = request.POST.get('kkkkk')
        yong = User.objects.get(id=cid)
        yong.login_type=0
        yong.save()
        # print('aaaabc',id)
        return render(request, 'tiao3.html', context={'a': '禁止成功','dizhi':"location.href='/admin/index/19/'"})

    return redirect('admin:login')


def yunyong(request):
    if request.method == 'POST':
        cid = request.POST.get('kkkkk')
        yong = User.objects.get(id=cid)
        yong.login_type=1
        yong.save()
        # print('aaaabc',id)
        return render(request, 'tiao3.html', context={'a': '已允许登陆','dizhi':"location.href='/admin/index/20/'"})

    return redirect('admin:login')


def xiashang(request):
    if request.method == 'POST':
        cid = request.POST.get('kkkkk')
        yong = Good.objects.get(id=cid)
        yong.isDelete=0
        yong.save()
        # print('aaaabc',id)
        return render(request, 'tiao3.html', context={'a': '已下架','dizhi':"location.href='/admin/index/7/1/'"})

    return redirect('admin:login')


def shangshang(request):
    if request.method == 'POST':
        cid = request.POST.get('kkkkk')
        yong = Good.objects.get(id=cid)
        yong.isDelete=1
        yong.save()
        # print('aaaabc',id)
        return render(request, 'tiao3.html', context={'a': '上架成功','dizhi':"location.href='/admin/index/11/1/'"})

    return redirect('admin:login')


def shanshang(request):
    if request.method == 'POST':
        cid = request.POST.get('kkkkk')
        yong = Good.objects.get(id=cid)
        yong.delete()
        # print('aaaabc',id)
        return render(request, 'tiao3.html', context={'a': '已删除','dizhi':"location.href='/admin/index/11/1/'"})

    return redirect('admin:login')


def xiushang(request,id):
    if request.session.get('username'):
        us = request.session.get('username')
        dbk = Aplate.objects.filter(aid=0)
        xbk = Aplate.objects.filter(aid__gte=1)
        shp = Good.objects.get(id=id)
        fen = Type.objects.get(id=shp.titleid)
        if request.method == 'POST':
            try:
                name = request.POST.get('ming')
                jian = request.POST.get('jian')
                jin = request.POST.get('jin')
                show = request.POST.get('show')
                huo = request.POST.get('huo')
                ku = request.POST.get('ku')
                xq1 = request.POST.get('fuw')
                fenlie = shp.titleid
                if xq1:
                    xq=xq1
                else:
                    xq=shp.xq

                file = request.FILES.get('photo')
                if file:
                    local_path = os.path.join(settings.UPLOAD_PATH,file.name)
                    path = local_path.replace("\\", '/')
                    # print(local_path)
                    # #文件类型过滤
                    ext = os.path.splitext(file.name)
                    # print(ext)
                    # print(len(ext))
                    # print(ext[1])
                    if len(ext) < 1 or not ext[1] in settings.ALLOWED_FILEEXTS:  # ALLOWED_FILEEXTS
                        # return redirect(reverse('upload'))
                        # return redirect('admin:upload')
                        # print(settings.ALLOWED_FILEEXTS)
                        # return HttpResponse('no')
                        return render(request, 'tiao2.html', context={'a': '图片格式不对'})

                    # 解决文件重名
                    if os.path.exists(path):

                        # 日期目录
                        dir = datetime.today().strftime("%Y/%m/%d")
                        # print('1',dir)
                        dir = os.path.join(settings.UPLOAD_PATH, dir)  # settings.MEDIA_ROOT
                        # print('2',dir)
                        if not os.path.exists(dir):
                            os.makedirs(dir)  # 递归创建目录
                        # list.png
                        file_name = ext[0] + datetime.today().strftime("%Y%m%d%H%M%S") + str(randint(1, 1000)) + ext[1] if len(
                            ext) > 1 else ''
                        path = os.path.join(dir, file_name).replace("\\", '/')  #
                    # print(path , type(path))
                    # ac = path
                    # print('ac',ac)


                    # 创建新文件
                    with open(path, 'wb') as fp:
                        # 如果文件超过2.5M,则分块读写
                        if file.multiple_chunks():
                            for block1 in file.chunks():
                                fp.write(block1)
                        else:
                            fp.write(file.read())
                    # return redirect(reverse('index'))
                    path1 = '/' + path
                    print(path, type(path))
                else:
                    path1=shp.pic
                kucu = int(ku)+(int(huo) * 1000)
                print('kkkkk', kucu)


                # if xiangxi:
                #     xiangx = xiangxi
                # else:
                #     xiangx = '<p>便宜的时候不多了,快来剁手吧.</p>'
                # print('dddd', xiangxi)
                # goods = Good(name=name, titleid=fenlie, pic=path1, price=show, costing=jin, kucun=kucu, content=jian,xq=xq)
                shp.name=name
                shp.titleid=fenlie
                shp.pic=path1
                shp.price=show
                shp.costing=jin
                shp.kucun=kucu
                shp.content=jian
                shp.xq=xq
                shp.save()
                return render(request, 'tiao4.html', context={'a': '修改成功', 'dizhi': "location.href='/admin/xiushang/",'did':id})
            except Exception as e:
                return render(request, 'tiao4.html', context={'a': '已删除', 'dizhi': "location.href='/admin/xiushang/",'did':id})

        return render(request, 'xiushang.html',context={'dbk': dbk, 'xbk': xbk, 'ming': Auser.objects.filter(name=us)[0],'shp':shp,'fen':fen})
    else:
        return redirect('admin:login')

def xiaoguan(request):
    dbk = Aplate.objects.filter(aid=0)
    xbk = Aplate.objects.filter(aid__gte=1)
    if request.method == 'POST':
        form = XiaoGuan(request.POST)
        # if form.is_valid():
        p1 = request.POST.get('fenlie')
        print('kkkhhhhhkkkk',p1)
        us = Auser.objects.get(id=p1)
        us.delete()
        return render(request, 'tiao3.html', context={'a': '已删除', 'dizhi': "location.href='/admin/index/39/'"})
    # else:
    #     return render(request, 'zhuce.html', context={'form': form, 'dbk': dbk, 'xbk': xbk,
    #                                                       'ming': request.session.get('username')})


def page_not_found(request):
    return render(request, 'tiao.html',context={'a':'404，对不起，您所访问的页面被外星人抓走了。'})

def page_inter_error(request):
    return render(request, 'tiao.html',context={'a':'500错误，不好意思哈.'})


