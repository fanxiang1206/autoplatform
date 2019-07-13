from django.db import models
from module.models import Module
# Create your models here.

class Case(models.Model):

    module = models.ForeignKey(Module,on_delete=models.CASCADE)
    name = models.CharField("用例名称",max_length=300)
    url = models.CharField("URL",max_length=300)
    method = models.CharField("请求方法",max_length=300)
    header = models.CharField("headers",max_length=300)
    param_type = models.CharField("参数类型",max_length=300)
    params = models.CharField("params",max_length=300)
    assert_type = models.CharField("断言类型",max_length=300)
    assert_params = models.CharField("断言参数",max_length=300)
    creattime = models.DateTimeField("创建时间",auto_now_add=True)

    def __str__(self):
        return self.name
