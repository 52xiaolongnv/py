# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import  Item,Field


class YiujobItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    job = Field()#科目
    jobcontent = Field()#具体科目
    pay = Field()#薪酬
    education = Field()#学历
    experience = Field()#经验
    welfare = Field()#福利
    title = Field()#标题
    time = Field()#发布时间
    city = Field()#城市
    quyu = Field()#区域
    name = Field()#公司名称
    content = Field()#内容
    jutidizhi = Field()#具体地址
    call = Field()#电话
    whereform = Field()#来自哪个网站
    title_url = Field()#正文的链接




