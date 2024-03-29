# Generated by Django 2.2.3 on 2019-07-13 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='用例名称')),
                ('url', models.CharField(max_length=300, verbose_name='URL')),
                ('method', models.CharField(max_length=300, verbose_name='请求方法')),
                ('header', models.CharField(max_length=300, verbose_name='headers')),
                ('param_type', models.CharField(max_length=300, verbose_name='参数类型')),
                ('params', models.CharField(max_length=300, verbose_name='params')),
                ('assert_type', models.CharField(max_length=300, verbose_name='断言类型')),
                ('assert_params', models.CharField(max_length=300, verbose_name='断言参数')),
                ('creattime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module.Module')),
            ],
        ),
    ]
