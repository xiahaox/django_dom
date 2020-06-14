# Generated by Django 2.0 on 2020-06-03 16:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='城市名称')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '城市信息',
                'verbose_name_plural': '城市信息',
            },
        ),
        migrations.CreateModel(
            name='OrgInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=200, upload_to='org/', verbose_name='机构封面')),
                ('name', models.CharField(max_length=200, verbose_name='机构名称')),
                ('course_num', models.IntegerField(default=0, verbose_name='课程数')),
                ('study_num', models.IntegerField(default=0, verbose_name='学习人数')),
                ('address', models.CharField(max_length=200, verbose_name='机构地址')),
                ('desc', models.CharField(max_length=200, verbose_name='机构简介')),
                ('detail', models.TextField(verbose_name='机构详情')),
                ('love_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('click_num', models.IntegerField(default=0, verbose_name='访问量')),
                ('category', models.CharField(choices=[('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')], max_length=10, verbose_name='机构类别')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('cityinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgs.CityInfo', verbose_name='所在城市')),
            ],
            options={
                'verbose_name': '机构信息',
                'verbose_name_plural': '机构信息',
            },
        ),
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=200, upload_to='teacher/', verbose_name='讲师头像')),
                ('name', models.CharField(max_length=20, verbose_name='讲师姓名')),
                ('work_year', models.IntegerField(default=0, verbose_name='工作年限')),
                ('work_position', models.CharField(max_length=20, verbose_name='工作职位')),
                ('work_style', models.CharField(max_length=200, verbose_name='教学特点')),
                ('age', models.IntegerField(default=30, verbose_name='讲师年龄')),
                ('gender', models.CharField(choices=[('girl', '女'), ('boy', '男')], default='boy', max_length=10, verbose_name='讲师性别')),
                ('love_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('click_num', models.IntegerField(default=0, verbose_name='访问量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('work_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgs.OrgInfo', verbose_name='所述机构')),
            ],
            options={
                'verbose_name': '讲师信息',
                'verbose_name_plural': '讲师信息',
            },
        ),
    ]