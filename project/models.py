from django.db import models

# Create your models here.
class Project(models.Model):

    name = models.CharField("名称",max_length=50,null=False)
    describe = models.TextField("描述",max_length=100)
    status = models.BooleanField("状态",default=1)
    creattime = models.DateTimeField("创建时间",auto_now_add=True)


    def __str__(self):
        return self.name
