import re
from django import forms
from django.core.exceptions import ValidationError
from Admin.models import Auser


# 验证单个字段
def check_password(value):
    if re.match(r'\d+$',value):
        raise ValidationError("密码不能是纯数字")



class ZhCe(forms.Form):
    username = forms.CharField(label='用户名',min_length=3,max_length=30,error_messages={'required':'必填','min_length':'最少3个字符','max_length':'最多30字符'})
    password1 = forms.CharField(label='密码', validators=[check_password], min_length=3, max_length=128,widget=forms.PasswordInput(), error_messages={'required': '必填','min_length': '最少3个字符','max_length': '最多128字符'})
    password2 = forms.CharField(label='确认密码', min_length=3, max_length=128, widget=forms.PasswordInput(),error_messages={'required': '必填', 'min_length': '最少3个字符', 'max_length': '最多128字符',})
    email = forms.EmailField(label='邮箱',error_messages={'required':'必填','invalid': "邮箱格式无效"})
    typee = forms.ChoiceField(choices=[(0, "超级管理员"), (1, "一级管理员"), (2, "二级管理员"),(3, "三级管理员")],label="权限",initial=0,required=False )

    def clean_username(self):
        name = self.cleaned_data.get('username')
        res = Auser.objects.filter(name=name).exists()
        if res:
            raise ValidationError("用户名重复")
        else:
            return name

    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        print(password1,password2)
        if password1 != password2:
            raise ValidationError({'password2':"两次密码不一致"})
        else:
            return self.cleaned_data


