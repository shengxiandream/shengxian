import re


from django import forms
from django.core.exceptions import ValidationError
from django.http import request

from Admin.models import Type, Good, Auser


# 验证单个字段
def check_password(value):
    if re.match(r'\d+$',value):
        raise ValidationError("密码不能是纯数字")


class ZhHu(forms.Form):
    # username = forms.CharField(label='用户名',min_length=3,max_length=30,error_messages={'required':'必填','min_length':'最少3个字符','max_length':'最多30字符'})
    password1 = forms.CharField(label='密码', validators=[check_password], min_length=3, max_length=128,widget=forms.PasswordInput(), error_messages={'required': '必填','min_length': '最少3个字符','max_length': '最多128字符'})
    password2 = forms.CharField(label='确认密码', min_length=3, max_length=128, widget=forms.PasswordInput(),error_messages={'required': '必填', 'min_length': '最少3个字符', 'max_length': '最多128字符',})
    # yzm = forms.CharField(label='邮箱验证码', min_length=6, max_length=6,error_messages={'required': '必填', 'min_length': '最少6个字符', 'max_length': '最多6字符'})
    # email = forms.EmailField(label='邮箱',error_messages={'required':'必填','invalid': "邮箱格式无效"})
    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        print(password1,password2)
        if password1 != password2:
            raise ValidationError({'password2':"两次密码不一致"})
        else:
            return self.cleaned_data

    # def clean_username(self):
    #     name = self.cleaned_data.get('username')
    #     res = Auser.objects.filter(name=name).exists()
    #     if res:
    #         return name
    #     else:
    #         raise ValidationError("用户名不存在")

    # def clean_yzm(self):
    #     yan1 = self.cleaned_data.get('yzm')
    #     yan2 = request.session.get('yzm')
    #     if yan1 != str(yan2):
    #         raise ValidationError("验证码错误")
    #     else:
    #         return yan1

class AddShang(forms.Form):
    fenlie = forms.ModelChoiceField(queryset=Type.objects.all())
    ming = forms.CharField(label='商品名称',max_length=30,error_messages={'required':'必填','max_length':'最多30字符'})
    jianjie = forms.CharField(label='简介',max_length=100,error_messages={'required':'必填','max_length':'最多100个字'})
    tupian = forms.ImageField(label='产品图片',error_messages={'required':'必传'})
    jinjia = forms.DecimalField(label='进价',decimal_places=2,error_messages={'required':'必填','decimal_places':'小数位最多两位'})
    shoujia = forms.DecimalField(label='进价', decimal_places=2,error_messages={'required': '必填', 'decimal_places': '小数位最多两位'})
    kucun = forms.IntegerField(label='库存',error_messages={'required': '必填'})


# class XiuShang(forms.Form):
#     fenlie = forms.ModelChoiceField(queryset=Type.objects.all())
#     id = request.session.get('ddid')
#     kk = Good.objects.get(id=id)
#     ming = forms.CharField(label='商品名称',max_length=30,error_messages={'required':'必填','max_length':'最多30字符'},initial=kk.name)
#     jianjie = forms.CharField(label='简介',max_length=100,error_messages={'required':'必填','max_length':'最多100个字'})
#     tupian = forms.ImageField(label='产品图片',error_messages={'required':'必传'})
#     jinjia = forms.DecimalField(label='进价',decimal_places=2,error_messages={'required':'必填','decimal_places':'小数位最多两位'})
#     shoujia = forms.DecimalField(label='进价', decimal_places=2,error_messages={'required': '必填', 'decimal_places': '小数位最多两位'})
#     kucun = forms.IntegerField(label='库存',error_messages={'required': '必填'})

class XiaoGuan(forms.Form):
    fenlie = forms.ModelChoiceField(queryset=Auser.objects.all())
