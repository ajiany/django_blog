from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    #手机号
    mobile=models.CharField(max_length=11,unique=True,blank=False)
    #头像信息
    avatar=models.ImageField(upload_to='avatar/%Y%m%d/',blank=True)
    #简介信息
    user_desc=models.CharField(max_length=500,blank=True)

    # 修改认证的字段为 手机号
    USERNAME_FIELD = 'mobile'

    #创建超级管理员必须输入的字段（不包括 手机号和密码）
    REQUIRED_FIELDS = ['username','email']
    # Mobile: 88888888
    # email: 88888888@qq.com
    # username: ajiany
    # password: xujiajian
    class Meta:
        db_table='tb_user'  #修改表名
        verbose_name='用户管理' #admin 后台显示
        verbose_name_plural=verbose_name #admin后台显示

    def __str__(self):
        return self.mobile
