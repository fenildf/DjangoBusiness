# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-15 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('abstract', models.CharField(max_length=128, verbose_name='摘要')),
                ('context', models.TextField(help_text='文章的正文内容', verbose_name='正文')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='NavigationItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=16, verbose_name='名称')),
                ('url', models.CharField(max_length=64, verbose_name='链接地址')),
                ('sequence', models.CharField(choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4)], max_length=1, unique=True, verbose_name='顺序')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='名称')),
                ('phone', models.CharField(default='', max_length=64, verbose_name='电话')),
                ('email', models.EmailField(default='', max_length=254, verbose_name='邮箱')),
                ('qq', models.CharField(max_length=16, verbose_name='QQ')),
                ('weibo', models.CharField(default='', max_length=32, verbose_name='微薄')),
                ('wechat', models.CharField(default='', max_length=16, verbose_name='微信')),
                ('address', models.CharField(default='', max_length=128, verbose_name='地址')),
                ('about_us', models.TextField(default='', max_length=4096, verbose_name='简介 ')),
                ('lock', models.CharField(default='U', max_length=1, unique=True, verbose_name='锁定')),
                ('cover', models.ForeignKey(help_text='主页封面', on_delete=django.db.models.deletion.CASCADE, related_name='cover', to='homepage.Document')),
                ('ico', models.ForeignKey(help_text='浏览器 ICO', on_delete=django.db.models.deletion.CASCADE, related_name='ico', to='homepage.Document')),
                ('logo', models.ForeignKey(help_text='公司 LOGO', on_delete=django.db.models.deletion.CASCADE, related_name='logo', to='homepage.Document')),
                ('qr_code', models.ForeignKey(help_text='微信二维码', on_delete=django.db.models.deletion.CASCADE, related_name='wechat', to='homepage.Document')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleItem',
            fields=[
                ('basearticle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='homepage.BaseArticle')),
                ('title2', models.CharField(blank=True, max_length=64, null=True, verbose_name='副标题')),
                ('sequence', models.CharField(choices=[('0', 0), ('1', 1), ('2', 2)], max_length=1, unique=True, verbose_name='顺序')),
                ('cover', models.ForeignKey(help_text='文章的封面图标', on_delete=django.db.models.deletion.CASCADE, to='homepage.Document')),
            ],
            bases=('homepage.basearticle',),
        ),
        migrations.CreateModel(
            name='HeaderItem',
            fields=[
                ('basearticle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='homepage.BaseArticle')),
                ('sequence', models.CharField(choices=[('0', 0), ('1', 1), ('2', 2)], max_length=1, unique=True, verbose_name='顺序')),
                ('cover', models.ForeignKey(help_text='文章的封面图标', on_delete=django.db.models.deletion.CASCADE, to='homepage.Document')),
            ],
            bases=('homepage.basearticle',),
        ),
    ]
